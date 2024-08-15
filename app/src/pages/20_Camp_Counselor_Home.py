import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Displaying welcome message for camp counselor
st.title(f"Welcome Camp Counselor, {st.session_state['first_name']}.")
# Adding some spacing between the title and the content
st.write('')
st.write('')
st.write('### What would you like to do today?')
# Button to navigate to the page for getting staff info
if st.button('Get Staff Information', 
             type='primary',
             use_container_width=True):
  # Switch to "Camp Counselor Staff Info" page
  st.switch_page('pages/21_Camp_Counselor_Staff_Info.py')
# Button to navigate to the page for deleting schedule information
if st.button('Delete Schedule Information', 
             type='primary',
             use_container_width=True):
  # Switch to "Camp Counselor Delete" page
  st.switch_page('pages/22_Camp_Counselor_Delete.py')
# Button to navigate to the page for updating activity description
if st.button("Update Actvity Description",
             type='primary',
             use_container_width=True):
  # Switch to "Camp Counselor Update Activity" page
  st.switch_page('pages/23_Camp_Counselor_Update_Activity.py')