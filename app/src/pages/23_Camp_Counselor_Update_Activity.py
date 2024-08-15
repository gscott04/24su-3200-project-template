import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
from datetime import date


SideBarLinks()

st.write("Update Your Activity!")

# Create a form for entering medical information
with st.form("Update activity description for August 8th, 2024 below"):
    # Input field for the new description
    c_info = st.text_input("Please write the new description")

    # Submit button for the form 
    submitted = st.form_submit_button("submit")
    if submitted: 
        # Create a dictionary to store the data
        data = {}
        data["description"] = c_info
        # Display the submitted data on the page 
        st.write(data)
        # Send a POST request to the API with the submitted data
        requests.put('http://api:4000/g/guardian', json = data)

'''
Enter the new description for today's activity
'''