import logging
import requests
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)

# Add sidebar navigation and logo to the Streamlit app
SideBarLinks()

# App main title
st.title("Guardian Information Lookup")

# Input for Camper ID
camper_id = st.number_input("Enter your Camper ID number:", step=1, key='camper_id')

# Button to trigger the information retrieval
if st.button('Get Guardian Info'):
    # API URL endpoint
    url = f'http://api:4000/d/camp_director/{camper_id}'
    
    # Make a request to the API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError for bad responses

        # If the response is successful
        if response.ok:
            guardian_data = response.json()
            if guardian_data:
                for item in guardian_data:
                    # Display each guardian's details
                    if 'campDirectorID' in item:
                        st.write(f"Guardian ID: {item['campDirectorID']}, First Name: {item['firstName']}, "
                                 f"Last Name: {item['lastName']}, Phone: {item['phone']}, Email: {item['email']}")
                    else:
                        st.error("Unexpected item structure.")
            else:
                st.warning("No guardian information available for the given ID.")
    except requests.RequestException as e:
        logger.error(f"Error fetching guardian info: {str(e)}")
        st.error(f"An error occurred: {str(e)}")

