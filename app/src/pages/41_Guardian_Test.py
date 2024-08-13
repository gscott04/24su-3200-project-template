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
        data["camperID"] = c_id
        data["medID"] = m_id
        st.write(data)

        requests.post('http://api:4000/g/guardian', json = data)


"""
Please enter in your camper's ID and the corresponding medical conditions ID
"""
