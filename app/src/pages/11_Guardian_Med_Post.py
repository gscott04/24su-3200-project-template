import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Show appropriate sidebar links 
SideBarLinks()

# Display page title for medical information input 
st.write("Medical Information Input")

# Create a form for entering medical information
with st.form("enter med info"):
    # Input field for the camperID
    c_id = st.text_input("input your camper's ID:")
    # Input field for the medical condition ID
    m_id = st.text_input("input the medical condition's ID:")
    # Submit button for the form 
    submitted = st.form_submit_button("submit")
    if submitted: 
        # Create a dictionary to store the data
        data = {}
        data["camperID"] = c_id
        data["medID"] = m_id
        # Display the submitted data on the page 
        st.write(data)
        # Send a POST request to the API with the submitted data
        requests.post('http://api:4000/g/guardian', json = data)


"""
Please enter in your camper's ID and the corresponding medical conditions ID
"""
