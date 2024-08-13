import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("Your Child's Conseler Contact")


# You can access the session state to make a more customized/personalized app experience
guardian = requests.get('http://api:4000/g/guardian').json()

try:
  st.dataframe(guardian)
except:
  st.write("Could not connect to database to get guardian!")