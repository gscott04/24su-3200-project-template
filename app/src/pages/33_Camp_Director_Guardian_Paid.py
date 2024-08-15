import logging
import streamlit as st
import pandas as pd
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

# Display the appropriate sidebar links
SideBarLinks()

# Display the page title 
st.title("Find guardians who haven't paid")

def get_data_from_api():
    url = 'http://api:4000/d/camp_director/unpaid'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error fetching guardians missing payments: {str(e)}")
        st.error(f"Failed to fetch guardians missing payments. Error: {str(e)}")
        return None

def json_to_dataframe(json_data):
    return pd.DataFrame(json_data)

def display_data():
    if st.button('Find Guardians Missing Payments', type='primary', use_container_width=True):
        json_data = get_data_from_api()
        if json_data:
            df = json_to_dataframe(json_data)
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("No data available or failed to fetch data.")

# Call the display function
display_data()