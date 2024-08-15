import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("Your Child's Counselor Contact Info")

camperID = st.number_input("Input your child's camper ID", step=1)

if st.button('Get Counselor Contact Info', type='primary', use_container_width=True):
    try:
        url = f'http://api:4000/g/guardian/CC/{camperID}'
        st.write(f"Requesting URL: {url}")
        
        response = requests.get(url)
        
        st.write(f"Response Status Code: {response.status_code}")
        
        if response.status_code == 200:
            try:
                counselor_contact = response.json()
                st.write(f"Contact info for your child with camper ID:{camperID}")
                if counselor_contact:
                    for item in counselor_contact:
                        st.write(f"Counselor Phone: {item['phoneNumber']}, Counselor Email: {item['email']}")
                else:
                    st.write("We are having trouble pulling up the counselor's contact info, please call the camp.")
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