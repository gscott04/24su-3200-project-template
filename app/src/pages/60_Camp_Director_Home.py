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

if st.button('Get Cabin Information', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/61_Camp_Director_Cabin_Info.py')

if st.button('View the Simple API Demo', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_API_Test.py')

if st.button("View Classification Demo",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Classification.py')