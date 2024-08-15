import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

# Streamlit page layout
st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()
# Displaying welcome message for guardian 
st.title(f"Welcome Guardian, {st.session_state['first_name']}.")
# Adding some spacing between the title and the content
st.write('')
st.write('')
st.write('### What would you like to do today?')

# Button to navigate to the page to enter medical information
if st.button("Enter medical information",
             type='primary',
             use_container_width=True):
  # Switch to the page to enter medical information
  st.switch_page('pages/11_Guardian_Med_Post.py')

# Button to navigate to the page to find required items for the day
if st.button('Find required items for the day', 
             type='primary',
             use_container_width=True):
  # Switch to the page to find required items for the day
  st.switch_page('pages/12_Guardian_Items.py')

# Button to reach out to a counselor
if st.button("Reach out to a counselor",
             type='primary',
             use_container_width=True):
  # Switch to the page to reach out to a counselor
  st.switch_page('pages/13_Guardian_contact.py')  