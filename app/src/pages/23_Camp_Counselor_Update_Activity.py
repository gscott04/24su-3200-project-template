import logging
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
from datetime import date

logger = logging.getLogger(__name__)

SideBarLinks()

st.write("Update an Activity!")

# Create a form for updating activity description
with st.form("Update activity description for August 8th, 2024 below"):
    # Input field for the new description
    
    activityID = st.number_input("Please enter the activity ID", step=1)
    description = st.text_input("Please write the new description")

    # Submit button for the form 
    submitted = st.form_submit_button("submit")
    if submitted: 
        # Create a dictionary to store the data
        data = {"description": description}
        data["description"] = description
        # Display the submitted data on the page 

        # Send a POST request to the API with the submitted data
        response = requests.put(f'http://api:4000/c/camp_counselor/{activityID}', json=data)
        response.raise_for_status()
        st.success("Activity updated successfully!")
'''
Enter the new description for today's activity
'''