
import streamlit as st
import pandas as pd 

#project_1_page = st.Page(
#page = "views/Superstore Sales Analysis Dashboard.py",
#title = "sales dashboard",
#icon = ":material/bar_chart:"
#)

#df = pd.read_csv(r"C:\Users\This PC\Downloads\archive(1)\train.csv")
# Example dataframe cleanup before display
#def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
   # df = df.convert_dtypes()
   # df = df.infer_objects(copy=False)
   # df = df.astype({col: "int64" for col in df.select_dtypes("Int64").columns})
    #return df


project_1_page = st.Page(
    page = "views/Superstore_Sales_Analysis_Dashboard.py",  # underscores
    title = "Sales Dashboard",
    icon = ":material/bar_chart:"
)
project_2_page = st.Page(
    page ="views/chat_bot.py",
    title = "Chat Bot",
    icon = ":material/smart_toy:"
)
project_3_page = st.Page(
    page ="views/about_me.py",
    title = "About Me",
    icon =":material/book:"
)
project_4_page = st.Page(
    page = "forms/contact.py",
    title = "Contacts",
    icon = ":material/contacts:"
)
#project_2_page = st.Page(
#page ="views/chatbot.py",
#title = "chat bot",
#icon =":material/smart_toy:"
#)

### -----NAVIGATION SETUP(WITHOUT SECTIONS) ------#### 
## pg = st.navigation(pages=[about_page, project_1_page, project_2_page])
# ----NAVIGATION SETUP [WITH SECTIONS]---- 
pg = st.navigation(
    {
        #"Info": [about_me],
        "Projects": [project_1_page, project_2_page,project_3_page, project_4_page],
    }
)
## -----SHARED ON ALL PAGES------ 
#st.logo("assets/iconic.png")
#st.image("assets/iconic.png", caption="My App Logo", use_column_width=True)
st.image("assets/iconic.png", use_container_width=True)
st.sidebar.text("Made with ❤️❤️❤️ by Baraka")

# ------RUN NAVIGATION------

pg.run()