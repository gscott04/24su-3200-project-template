import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Camp Director, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View Cabin Information', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/61_Camp_Director_Cabin_Info.py')

if st.button('Get a Guardians Contact Info', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/62_Camp_Director_Guardian_Info.py')

if st.button("Find Guardians Missing Payments",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/63_Camp_Director_Guardian_Paid.py')