
import streamlit as st
import pandas as pd 


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

pg = st.navigation(
    {
        #"Info": [about_me],
        "Projects": [project_1_page, project_2_page,project_3_page, project_4_page],
    }
)

st.image("assets/iconic.png", use_container_width=True)
st.sidebar.text("Made with ❤️❤️❤️ by Baraka")

# ------RUN NAVIGATION------

pg.run()