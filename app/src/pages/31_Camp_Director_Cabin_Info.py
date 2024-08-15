import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Show appropriate sidebar links
SideBarLinks()

# Display the title for cabin information section 
st.write("View Cabin Information for Staff")

# Input field for staffID
staffID = st.number_input("Enter the staff ID to find the cabin they're staying in", step=1)

# Button to trigger fetching cabin info for provided staffID
if st.button('Get Cabin Info', type='primary', use_container_width=True):
    try:
        # Send a GET request to the API with the staffID
        url = f'http://api:4000/d/camp_director/{staffID}'
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the response as JSON from the API
            cabin_data = response.json()
            # Dislay the cabin information for the staff member
            st.write(f"Cabin info for the staff member (Staff ID: {staffID})")
            if cabin_data:
                # Loop through the cabin data and display the cabin information
                for item in cabin_data:
                    if 'cabinID' in item:
                        # Check if there is no Cabin Name (Camps are not required to name Cabins)
                        if item['cabinName'] is None:
                            st.write(f"Cabin ID: {item['cabinID']}")
                        # If there is a Cabin Name, return it with the Cabin ID
                        if item['cabinName'] is not None:
                            st.write(f"Cabin Name: {item['cabinName']}, Cabin ID: {item['cabinID']}")
                    # Error messages
                    else:
                        st.write(f"Unexpected item structure: {item}")
            else:
                st.write("No cabin information available for that staff member.")
        else:
            st.error(f"Failed to fetch cabin info. Status code: {response.status_code}")
            st.write("Response Content:")
            st.code(response.text)
    except requests.RequestException as e:
        logger.error(f"Error fetching cabin info: {str(e)}")
        st.error(f"Failed to fetch cabin info. Error: {str(e)}")