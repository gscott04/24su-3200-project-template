import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("Find Guardian Information")


guardianID = st.number_input("Enter your ID number:", step=1)

if st.button('Get Guardian IDs', type='primary', use_container_width=True):
    try:
        url = f'http://api:4000/d/camp_director/{guardianID}'
        response = requests.get(url)
        
        if response.status_code == 200:
            guardian_data = response.json()
            st.write(f"Guardian ID for your camper: (Guardian ID: {guardianID})")
            if guardian_data:
                for item in guardian_data:
                    if 'campDirectorID' in item:
                        st.write(f"Guardian First Name: {item['firstName']}, Guardian Last Name: {item['lastName']}, 
                                 Guardian Phone Number: {item['phone']}, Guardian Email: {item['email']}")
                    else:
                        st.write(f"Unexpected item structure: {item}")
            else:
                st.write("No guardian information available for your camper.")
        else:
            st.error(f"Failed to fetch director info. Status code: {response.status_code}")
            st.write("Response Content:")
            st.code(response.text)
    except requests.RequestException as e:
        logger.error(f"Error fetching guardian info: {str(e)}")
        st.error(f"Failed to fetch guardian info. Error: {str(e)}")