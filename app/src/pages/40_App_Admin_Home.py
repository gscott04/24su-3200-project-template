import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome App Admin, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Find the camp directors', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/71_App_Admin_DirectorID.py')  

if st.button('Reach out to some guardians', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/72_App_Admin_Contact.py')

if st.button('Reach out to your camps', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/73_App_Admin_Camp_Contact.py')