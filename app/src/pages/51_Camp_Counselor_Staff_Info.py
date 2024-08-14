import logging
import requests
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)

# Add sidebar navigation and logo to the Streamlit app
SideBarLinks()
add_logo(st.sidebar)

# App main title
st.title("Staff Information Lookup")

# Input for Camp ID
campID = st.number_input("Enter your Camp ID number:", step=1, key='campID')

# Button to trigger the information retrieval
if st.button('Get Staff Info'):
    # API URL endpoint
    url = f'http://api:4000/camp_counselor/{staffID}'
    
    # Make a request to the API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError for bad responses

        # If the response is successful
        if response.ok:
            staffID_data = response.json()
            if staffID_data:
                for item in staffID_data:
                    # Display each staff's details
                    if 'campID' in item:
                        st.write(f"Staff ID: {item['staffID']}, First Name: {item['firstName']}, "
                                 f"Last Name: {item['lastName']}, Phone: {item['phone']}, Email: {item['email']}")
                    else:
                        st.error("Unexpected item structure.")
            else:
                st.warning("No staff information available for the given ID.")
    except requests.RequestException as e:
        logger.error(f"Error fetching staff info: {str(e)}")
        st.error(f"An error occurred: {str(e)}")

