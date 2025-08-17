# sales_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

## Suppress warnings:
import warnings
warnings.filterwarnings('ignore')
st.set_page_config(layout='wide')


## Load Data:
@st.cache_data
def load_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        # Fallback for development (assume relative path or hardcoded for testing)
        st.warning("No file uploaded. Using default path for demonstration.")
        path = r"C:\Users\This PC\Downloads\archive(1)\train.csv"  # Replace with your actual fallback path
        df = pd.read_csv(path)

    ## Handle Postal Code:
    if 'Postal Code' in df.columns:
        df['Postal Code'].fillna(0, inplace=True)
        df['Postal Code'] = pd.to_numeric(df['Postal Code'], errors="coerce").fillna(0).astype(int)

    ## Handle Order Date:
    if 'Order Date' in df.columns:
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors="coerce",format='%d/%m/%Y')  # Changed to '%d/%m/%Y' to match DD/MM/YYYY format
    else:
        st.error("Missing 'Order Date' column in data.")
        st.stop()

    ##  Convert nullable integers or objects to PyArrow-safe types:
    for col in df.columns:
        if pd.api.types.is_integer_dtype(df[col]) or pd.api.types.is_float_dtype(df[col]):
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        elif pd.api.types.is_object_dtype(df[col]):
            # Try converting to numeric if possible, otherwise leave as string
            try:
                df[col] = pd.to_numeric(df[col], errors='ignore')
            except:
                df[col] = df[col].astype(str)

    return df


uploaded_file = st.sidebar.file_uploader("Upload Superstore CSV", type="csv")
df = load_data(uploaded_file)
if df is None:
    st.error("Please upload a CSV file to proceed.")
    st.stop()

st.title("📊 Superstore Sales Analysis Dashboard")

## Sidebar options:
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose a view",
    [
        "Overview",
        "Customer Segment Analysis",
        "Sales by State (Choropleth)",
        "Product Category Sales",
        "Time Series Analysis"
    ],
    index=0  # Default to "Overview"
)


# 1. Overview
if option == "Overview":
    st.subheader("📌 Dataset Overview")
    st.write(df.head())
    st.write("Shape:", df.shape)
    st.write("Null values:", df.isnull().sum())
    st.write("Data Types:")
    st.write(df.dtypes)

# 2. Customer Segment
elif option == "Customer Segment Analysis":
    st.subheader("👥 Customer Segments")
    if 'Segment' not in df.columns:
        st.error("Missing 'Segment' column in data.")
        st.stop()
    segment_count = df['Segment'].value_counts().reset_index()
    segment_count.columns = ['Segment', 'Count']
    fig1, ax1 = plt.subplots()
    ax1.pie(segment_count['Count'], labels=segment_count['Segment'], autopct='%1.1f%%', colors=['#ff9999', '#66b3ff', '#99ff99'])
    st.pyplot(fig1)


# 3. Sales by State
elif option == "Sales by State (Choropleth)":
    st.subheader("🗺️ Total Sales by US State")
    if 'State' not in df.columns or 'Sales' not in df.columns:
        st.error("Missing 'State' or 'Sales' column in data.")
        st.stop()
    all_state_mapping = {
        "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
        "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
        "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID",
        "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
        "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
        "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS",
        "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
        "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
        "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
        "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
        "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
        "Vermont": "VT", "Virginia": "VA", "Washington": "WA", "West Virginia": "WV",
        "Wisconsin": "WI", "Wyoming": "WY"
    }
    df['Abbreviation'] = df['State'].map(all_state_mapping)
    state_sales = df.groupby('State')['Sales'].sum().reset_index()
    state_sales['Abbreviations'] = state_sales['State'].map(all_state_mapping)
    fig = go.Figure(data=go.Choropleth(
        locations=state_sales['Abbreviations'],
        locationmode='USA-states',
        z=state_sales['Sales'],
        showscale=True,
        colorscale='Reds'  # Changed to 'Reds' for better heat representation
    ))
    fig.update_layout(geo_scope='usa', title='Sales by US State')
    st.plotly_chart(fig, use_container_width=True)


# 4. Product Category
elif option == "Product Category Sales":
    st.subheader("📦 Product Category Performance")
    if 'Category' not in df.columns or 'Sales' not in df.columns:
        st.error("Missing 'Category' or 'Sales' column in data.")
        st.stop()
    category_sales = df.groupby('Category')['Sales'].sum().reset_index()
    fig2, ax2 = plt.subplots()
    ax2.pie(category_sales['Sales'], labels=category_sales['Category'], autopct='%1.1f%%', colors=['#ff9999', '#66b3ff', '#99ff99'])
    st.pyplot(fig2)


# 5. Time Series
elif option == "Time Series Analysis":
    st.subheader("📅 Sales Over Time")
    if 'Order Date' not in df.columns or 'Sales' not in df.columns:
        st.error("Missing 'Order Date' or 'Sales' column in data.")
        st.stop()
    df_monthly = df.set_index('Order Date').resample('M')['Sales'].sum().reset_index()
    fig3, ax3 = plt.subplots()
    ax3.plot(df_monthly['Order Date'], df_monthly['Sales'], marker='o')
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Sales")
    ax3.set_title("Monthly Sales Over Time")
    st.pyplot(fig3)