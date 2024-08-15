import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Display appropriate sidebar links
SideBarLinks()

# Display page title
st.write("Find a guardian's contact information")

# Input field for adminID
adminID = st.number_input("Enter your ID number", step=1)
# Button to get the contact info for guardians based on the adminID
if st.button('Get Contact Info', type='primary', use_container_width=True):
    try:
        # Send a GET request to the API with the adminID
        url = f'http://api:4000/a/app_admin/{adminID}'
        response = requests.get(url)
        # Parse the response as JSON from the API
        if response.status_code == 200:
            try:
                guardian_contact = response.json()
                # Display guardian contact information 
                st.write(f"Contact info for guardians based on your ID: {adminID}")
                if guardian_contact:
                    # Loop through the guardian contact data and display the contact information
                    for item in guardian_contact:
                        st.write(f"Guardian Phone: {item['phone']}, Guardian Email: {item['email']}")
                # Error messages
                else:
                    st.write(f"No contact information available for your camps.")
            except ValueError as json_error:
                st.error(f"Failed to parse JSON response. Error: {str(json_error)}")
                st.write(f"Response Content:")
                st.code(response.text)
        else:
            st.error(f"Failed to fetch contact info. Status code: {response.status_code}")
            st.write(f"Response Content:")
            st.code(response.text)
    except requests.RequestException as e:
        logger.error(f"Error fetching contact info: {str(e)}")
        st.error(f"Failed to fetch contact info. Error: {str(e)}")