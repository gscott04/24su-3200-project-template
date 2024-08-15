import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Guardian, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button("Enter medical information",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Guardian_Med_Post.py')

if st.button('Find required items for the day', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Guardian_DailySchedule.py')

if st.button("Reach out to a counselor",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Guardian_contact.py')  


