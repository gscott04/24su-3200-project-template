import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Camp Counselor, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Get Staff Information', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Camp_Counselor_Staff_Info.py')

if st.button('Delete Schedule Information', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_Camp_Counselor_Delete.py')

if st.button("Update Actvity Description",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Camp_Counselor_Update_Activity.py')