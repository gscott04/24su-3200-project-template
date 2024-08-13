import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# Find today's daily schedule!")

guardian = requests.get('http://api:4000/g/guardian/<c_date>').json()

try:
  st.dataframe(guardian)
except:
  st.write("Could not connect to database to get guardian!")