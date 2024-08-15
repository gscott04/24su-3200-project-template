import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
from datetime import date

# Display the appropriate sidebar links
SideBarLinks()

# Set up logging 
logger = logging.getLogger(__name__)

# Page title 
st.write("# Delete today's daily schedule!")

# Input fields for campID and sessionID
campID = st.text_input("Enter the camp ID:", "")
sessionID = st.text_input("Enter the session ID:", "")

# Date to be deleted (fixed for now)
date_to_delete = "7/27/2024"

if st.button('Delete Schedule', type ="primary", use_container_width=True):
    # Construct the DELETE request URL 
    delete_url = f'http://api:4000/c/camp_counselor/{campID}/{sessionID}'
    # Send delete request 
    response = requests.delete(delete_url)
    # Handling the response 
    if response.status_code == 200: 
        st.success('Daily schedule deleted successfully!')
    else: 
        st.error(f"Failed to delete schedule. Error code: {response.status_code}")
        

