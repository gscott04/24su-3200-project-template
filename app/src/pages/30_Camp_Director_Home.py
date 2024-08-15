import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

# Streamlit page layout
st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Displaying welcome message for camp director
st.title(f"Welcome Camp Director, {st.session_state['first_name']}.")
# Adding some spacing between the title and the content
st.write('')
st.write('')
st.write('### What would you like to do today?')
# Button to navigate to the page for getting cabin information
if st.button('View Cabin Information', 
             type='primary',
             use_container_width=True):
  # Switch to "Camp Director Cabin Info" page
  st.switch_page('pages/31_Camp_Director_Cabin_Info.py')
# Button to navigate to the page for getting guardian contact information
if st.button('Get a Guardians Contact Info', 
             type='primary',
             use_container_width=True):
  # Switch to "Camp Director Guardian Info" page
  st.switch_page('pages/32_Camp_Director_Guardian_Info.py')
# Button to navigate to the page for finding guardians missing payments
if st.button("Find Guardians Missing Payments",
             type='primary',
             use_container_width=True):
  # Switch to "Camp Director Guardian Paid" page
  st.switch_page('pages/33_Camp_Director_Guardian_Paid.py')