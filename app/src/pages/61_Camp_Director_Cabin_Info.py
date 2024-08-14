import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("View Cabin Information")

cabinID =st.number_input("Enter the cabin you want to get information from", step=1)

if st.button('Get Cabin IDs', type='primary', use_container_width=True):
    try:
        url = f'http://api:4000/d/camp_director/{cabinID}'
        response = requests.get(url)
        
        if response.status_code == 200:
            cabin_data = response.json()
            st.write(f"Cabin IDs in the camp (Cabin ID: {cabinID})")
            if cabin_data:
                for item in cabin_data:
                    if 'cabinID' in item:
                        st.write(f"Cabin Name: {item['cabinName']}")
                    else:
                        st.write(f"Unexpected item structure: {item}")
            else:
                st.write("No cabin information available for your camp.")
        else:
            st.error(f"Failed to fetch director info. Status code: {response.status_code}")
            st.write("Response Content:")
            st.code(response.text)
    except requests.RequestException as e:
        logger.error(f"Error fetching cabin info: {str(e)}")
        st.error(f"Failed to fetch cabin info. Error: {str(e)}")