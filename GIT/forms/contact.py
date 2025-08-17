


import streamlit as st 
import re 
import requests

#WEBHOOK_URL = st.secrets["WEBHOOK_URL"]
WEBHOOK_URL ="https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZhMDYzZTA0MzU1MjY4NTUzNzUxM2Ei_pc"

def is_valid_email(email):
    #Basic regex pattern for email validation:
    email_pattern = r"^[a-zA-z0-9_.+-] +@[a-zA-z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_area("Email Adress")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
    # st.success("Message successfully sent!")
        if not WEBHOOK_URL: 
            st.error("Email service is not set up. Please try again later.", icon="✉️✉️")
            st.stop()

        if not name:
            st.error("Please provide your name.", icon="🦂")
            st.stop()

        if not email:
            st.error("Pleasse provide your email address.", icon="✉️")
            st.stop()
        
        if not message:
            st.error("Please provide a message.", icon="✉️")
            st.stop()

    # Prepare the data payload and send it to the specified webhook URL:
    data = {"email": email, "name":name, 'message':message}
    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 200:
        st.sucess("Your message has been sent successfuly! 🎉", icon="🚀")
    else:
        st.error("There was an error sending your message.", icon="😌")




