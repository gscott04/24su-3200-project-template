import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Add sidebar navigation and logo to the Streamlit app
SideBarLinks()

# App main title
st.title("Guardian Information Lookup")

# Input for Camper ID
camperID = st.number_input("Enter your Camper ID number:", step=1)

# Button to trigger the information retrieval
if st.button('Get Guardian Info'):

    # Make a request to the API URL endpoint
    try:
        url = f'http://api:4000/d/camp_director/G/{camperID}'
        response = requests.get(url)

        # If the response is successful
        if response.status_code == 200:
            guardian_data = response.json()
            if guardian_data:
                for item in guardian_data:
                    # Display each guardian's details
                    if 'guardianID' in item:
                        st.write(f"Guardian ID: {item['guardianID']}, First Name: {item['firstName']}, Last Name: {item['lastName']}, Phone: {item['phone']}, Email: {item['email']}")
                    else:
                        st.write(f"Unexpected item structure: {item}")
            else:
                st.warning("No guardian information available for the given ID.")
    except requests.RequestException as e:
        logger.error(f"Error fetching guardian info: {str(e)}")
        st.error(f"An error occurred: {str(e)}")

