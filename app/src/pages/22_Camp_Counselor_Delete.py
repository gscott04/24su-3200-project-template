import logging
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

# Display the appropriate sidebar links
SideBarLinks()

# Page title 
st.title("Delete an unscheduled activity")

# Input field for activity ID
activityID = st.number_input("Enter the activity ID you wish to delete (hint: activities 42-90 are unscheduled):", step=1, min_value=42, max_value=91)

# When button pressed
if st.button('Delete Activity', type ="primary", use_container_width=True):
    # Construct the DELETE request URL 
    delete_url = f'http://api:4000/c/camp_counselor/{activityID}'
    # Send delete request 
    response = requests.delete(delete_url)
    # Handling the response 
    if response.status_code == 200: 
        st.success('Activity deleted successfully!')
    else: 
        st.error(f"Failed to delete activity. Error code: {response.status_code}")



