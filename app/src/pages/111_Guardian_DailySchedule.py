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

selected_date = st.date_input("Select a date", datetime.now())
if st.button("Get Schedule"):
    # Convert the date to string format YYYY-MM-DD
    date_str = selected_date.strftime("%Y-%m-%d")
    
    # Make the GET request to your Flask API
    response = requests.get(f"http://localhost:5000/guardian/{date_str}")
    
    if response.status_code == 200:
        data = response.json()
        if data:
            st.subheader(f"Schedule for {date_str}")
            for item in data:
                st.write(f"Date: {item['date']}")
                st.write(f"Required Items: {item['requiredItems']}")
        else:
            st.info("No schedule found for this date.")
    else:
        st.error("Failed to retrieve schedule. Please try again.")