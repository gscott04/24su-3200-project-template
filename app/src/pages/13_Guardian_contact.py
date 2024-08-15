import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Display the appropriate sidebar links
SideBarLinks()

# Display page title for counselor contact info 
st.write("Your Child's Counselor Contact Info")
# number input for the user to enter camperID
camperID = st.number_input("Input your child's camper ID", step=1, min_value=1, max_value=40)
# Button to trigger fetching counselor contact info 
if st.button('Get Counselor Contact Info', type='primary', use_container_width=True):
    try:
        # Send a GET request to the API with the camperID
        url = f'http://api:4000/g/guardian/CC/{camperID}'
        response = requests.get(url)
        if response.status_code == 200:
            try:
                # Parse the response as JSON 
                counselor_contact = response.json()
                # Display the counselors contact information
                st.write(f"Contact info for your child with camper ID:{camperID}")
                if counselor_contact:
                    for item in counselor_contact:
                        st.write(f"Counselor Name: {item['firstName']} {item['lastName']}, Counselor Phone: {item['phoneNumber']}, Counselor Email: {item['email']}")
                # Error messages 
                else:
                    st.write("We are having trouble pulling up the counselor's contact info, please call the camp.")
            except ValueError as json_error:
                st.error(f"Failed to parse JSON response. Error: {str(json_error)}")
                st.write("Response Content:")
                st.code(response.text)
        else:
            st.error(f"Failed to fetch contact info. Status code: {response.status_code}")
            st.write("Response Content:")
            st.code(response.text)
    except requests.RequestException as e:
        logger.error(f"Error fetching contact info: {str(e)}")
        st.error(f"Failed to fetch contact info. Error: {str(e)}")