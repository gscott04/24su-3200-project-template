import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("Find a camp's contact information")

campID = st.number_input("Enter a camp ID number 34098", step=1)

if st.button('Get Contact Info', type='primary', use_container_width=True):
    try:
        # GET request to Flask route
        url = f'http://api:4000/a/app_admin/{campID}'
        st.write(f"Requesting URL: {url}")
        
        response = requests.get(url)
        
        st.write(f"Response Status Code: {response.status_code}")
        st.write(f"Response Headers: {response.headers}")
        
        if response.status_code == 200:
            if 'application/json' in response.headers.get('Content-Type', ''):
                try:
                    camp_contact = response.json()
                    st.write(f"Contact info for Camp {campID}")
                    if isinstance(camp_contact, list) and len(camp_contact) > 0:
                        for item in camp_contact:
                            st.write(f"Camp Phone: {item[0]}, Camp Email: {item[1]}")
                    else:
                        st.write("No contact information available for this camp.")
                except ValueError as json_error:
                    st.error(f"Failed to parse JSON response. Error: {str(json_error)}")
            else:
                st.error("Response is not in JSON format")
                st.write("Response Content (first 500 characters):")
                st.code(response.text[:500])
        else:
            st.error(f"Failed to fetch contact info. Status code: {response.status_code}")
            st.write("Response Content (first 500 characters):")
            st.code(response.text[:500])
    except requests.RequestException as e:
        logger.error(f"Error fetching contact info: {str(e)}")
        st.error(f"Failed to fetch contact info. Error: {str(e)}")