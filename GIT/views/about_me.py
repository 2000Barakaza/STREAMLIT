import os
import sys
import streamlit as st

# Add parent folder to sys.path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from forms.contact import contact_form

# --- HERO SECTION ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
image_path = os.path.join(ROOT_DIR, "assets", "Baraka.jpg")

#def show_contact_form():
  #  import streamlit as st
#from forms.contact import contact_form

# Function to show contact form using the correct st.dialog API
@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


col1, col2 = st.columns(2, gap="small")
with col1:
    if os.path.exists(image_path):
        st.image(image_path, width=230)
    else:
        st.error(f"Image not found at {image_path}")
with col2:
    st.title("Baraka Manjale", anchor=False)
    st.write(
        "Intermediated AI/ML Engineer, Senior Data Analyst, Data Scientist, NLP Engineer, Data Scraping, Scrawling, Wrangling Expert and etc."
    )
    if st.button("📧✉️📩 Contact Me"):
        show_contact_form()
