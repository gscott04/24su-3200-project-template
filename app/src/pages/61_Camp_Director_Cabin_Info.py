import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("View Cabin Information for Staff")

staffID =st.number_input("Enter the staff ID to find the cabin they're staying in", step=1)

if st.button('Get Cabin Info', type='primary', use_container_width=True):
    try:
        url = f'http://api:4000/d/camp_director/{staffID}'
        response = requests.get(url)
        
        if response.status_code == 200:
            cabin_data = response.json()
            st.write(f"Cabin info for the staff member (Staff ID: {staffID})")
            if cabin_data:
                for item in cabin_data:
                    if 'cabinID' in item:
                        # check if there is no Cabin Name (Camps are not required to name Cabins)
                        if item['cabinName'] is None:
                            st.write(f"Cabin ID: {item['cabinID']}")
                        # if there is a Cabin Name, return it with the Cabin ID
                        if item['cabinName'] is not None:
                            st.write(f"Cabin Name: {item['cabinName']}, Cabin ID: {item['cabinID']}")
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