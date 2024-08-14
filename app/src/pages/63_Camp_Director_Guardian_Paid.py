import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("Find guardians who haven't paid.")

if st.button('Missing payment', type='primary', use_container_width=True):
    try:
        url = f'http://api:4000/camp_director/unpaid'
        response = requests.get(url)
        
        
    except requests.RequestException as e:
        logger.error(f"Error fetching guardians missing payments: {str(e)}")
        st.error(f"Failed to fetch guardians missing payments. Error: {str(e)}")