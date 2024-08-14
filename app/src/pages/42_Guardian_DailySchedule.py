import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
from datetime import date

SideBarLinks()

st.write("# Find today's daily schedule!")

c_date = st.date_input("Select a date between 7/22/24 and 8/31/24 or 2016/07/29", value=date.today())

if st.button('Get Schedule', type='primary', use_container_width=True):
    
    try:
        # Format the date as a string in the desired format (YYYY-MM-DD)
        formatted_date = c_date.strftime('%Y-%m-%d')
        
        # GET request to Flask route with the formatted date
        response = requests.get(f'http://api:4000/g/guardian/{formatted_date}')
        
        if response.status_code == 200:
            # If the request is successful, parse the JSON response
            schedule_data = response.json()
            
            # Display the schedule data
            st.write(f"Items required for {formatted_date}:")
            for item in schedule_data:
                st.write(f"Date: {item['date']}, Required Items: {item['requiredItems']}")
        elif response.status_code == 404:
            st.error(f"No schedule found for the date: {formatted_date}")
        else:
            st.error(f"Failed to fetch schedule. Status code: {response.status_code}")
    except requests.RequestException as e:
        logger.error(f"Error fetching schedule: {str(e)}")
        st.error("Failed to fetch schedule. Please check your connection and try again.")