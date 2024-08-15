import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("Find Camp Director ID")

adminID = st.number_input("Enter your ID number 2390", step=1)

if st.button('Get Director IDs', type='primary', use_container_width=True):
    try:
        url = f'http://api:4000/a/app_admin/CD/{adminID}'
        response = requests.get(url)
        
        if response.status_code == 200:
            director_data = response.json()
            st.write(f"Director IDs for your camps (Admin ID: {adminID})")
            if director_data:
                for item in director_data:
                    if 'campDirectorID' in item:
                        st.write(f"Camp Director ID: {item['campDirectorID']}")
                    else:
                        st.write(f"Unexpected item structure: {item}")
            else:
                st.write("No director information available for your camps.")
        else:
            st.error(f"Failed to fetch director info. Status code: {response.status_code}")
            st.write("Response Content:")
            st.code(response.text)
    except requests.RequestException as e:
        logger.error(f"Error fetching director info: {str(e)}")
        st.error(f"Failed to fetch director info. Error: {str(e)}")