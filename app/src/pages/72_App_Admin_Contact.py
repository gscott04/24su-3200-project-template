import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("Find your camps' contact information")

adminID = st.number_input("Enter your ID number 2390", step=1)

if st.button('Get Contact Info', type='primary', use_container_width=True):
    try:
        url = f'http://api:4000/a/app_admin/{adminID}'
        st.write(f"Requesting URL: {url}")
        
        response = requests.get(url)
        
        st.write(f"Response Status Code: {response.status_code}")
        
        if response.status_code == 200:
            try:
                camp_contact = response.json()
                st.write(f"Contact info for your camps {adminID}")
                if camp_contact:
                    for item in camp_contact:
                        st.write(f"Camp Phone: {item['phone']}, Camp Email: {item['email']}")
                else:
                    st.write("No contact information available for your camps.")
            except ValueError as json_error:
                st.error(f"Failed to parse JSON response. Error: {str(json_error)}")
                st.write("Response Content:")
                st.code(response.text)
        else:
            st.error(f"Failed to fetch contact info. Status code: {response.status_code}")
            st.write("Response Content:")
            st.code(response.text)
    except requests.RequestException as e:
        logger.error(f"Error fetching contact info: {str(e)}")
        st.error(f"Failed to fetch contact info. Error: {str(e)}")