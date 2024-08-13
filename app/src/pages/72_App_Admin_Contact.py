import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("Your camp's contact information")

# You can access the session state to make a more customized/personalized app experience
admin = requests.get('http://api:4000/a/app_admin').json()

try:
  st.dataframe(admin)
except:
  st.write("Could not connect to database to get guardian!")