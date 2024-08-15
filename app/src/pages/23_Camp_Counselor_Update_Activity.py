import logging
import streamlit as st
import requests
import json
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
from datetime import date

logger = logging.getLogger(__name__)

SideBarLinks()

st.write("Update an Activity!")

# Create a form for updating activity description
with st.form("Update activity description for August 8th, 2024 below"):
    # Input fields
    activityID = st.number_input("Please enter the activity ID", step=1)
    description = st.text_input("Please write the new description")
    
    # Submit button for the form 
    submitted = st.form_submit_button("Submit")
    
if submitted: 
    # Create a dictionary to store the data
    data = {"description": description}
    
    # Convert the data to JSON
    json_data = json.dumps(data)
    
    # Display the JSON data (optional, for debugging)
    st.json(json_data)
    
    try:
        # Send a PUT request to the API with the JSON data
        response = requests.put(f'http://api:4000/c/camp_counselor/{activityID}', 
                                data=json_data, 
                                headers={'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            st.success("Activity updated successfully!")
        
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while connecting to the API: {e}")
        logger.error(f"Error updating activity: {e}")