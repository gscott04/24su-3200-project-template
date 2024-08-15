import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
from datetime import date


SideBarLinks()

st.write("Update Your Activities!")

# Create a form for entering medical information
with st.form("enter med info"):
    # Input field for the camperID
    c_info = st.text_input("Please write the new description")
    # Input field for the medical condition ID
    # Submit button for the form 
    submitted = st.form_submit_button("submit")
    if submitted: 
        # Create a dictionary to store the data
        data = {}
        data["description"] = c_info
        # Display the submitted data on the page 
        st.write(data)
        # Send a POST request to the API with the submitted data
        requests.post('http://api:4000/g/guardian', json = data)


"""
Enter the new description for today's activity
"""