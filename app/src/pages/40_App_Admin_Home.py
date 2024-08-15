import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Displaying welcome message for app admin
st.title(f"Welcome App Admin, {st.session_state['first_name']}.")
# Adding some spacing between the title and the content
st.write('')
st.write('')
st.write('### What would you like to do today?')
# Button to navigate to page for finding camp directors 
if st.button('Find the camp directors', 
             type='primary',
             use_container_width=True):
  # Switch to "App Admin Camp Director" page
  st.switch_page('pages/41_App_Admin_DirectorID.py')  
# Button to navigate to page for contacting guardians
if st.button('Reach out to some guardians', 
             type='primary',
             use_container_width=True):
  # Switch to "App Admin Contact" page
  st.switch_page('pages/42_App_Admin_Contact.py')
# Button to navigate to page for contacting camps
if st.button('Reach out to your camps', 
             type='primary',
             use_container_width=True):
  # Switch to "App Admin Camp Contact" page
  st.switch_page('pages/43_App_Admin_Camp_Contact.py')