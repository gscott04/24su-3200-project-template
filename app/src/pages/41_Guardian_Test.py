import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("Medical Information Input")

with st.form("enter med info"):
    c_id = st.text_input("input your camper's ID:")
    m_id = st.text_input("input the medical condition's ID:")
    

    submitted = st.form_submit_button("submit")

    if submitted: 
        data = {}
        data["camper ID"] = c_id
        data["medical ID"] = m_id
        st.write(data)

        requests.post('http://api:4000/g/gaurdian', json = data)


"""
Simply retrieving data from a REST api running in a separate Docker Container.

If the container isn't running, this will be very unhappy.  But the Streamlit app 
should not totally die. 
"""
"""
data = {} 
try:
  data = requests.get('http://api:4000/data').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)
"""
