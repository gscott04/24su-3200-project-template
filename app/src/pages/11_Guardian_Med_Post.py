import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
import pandas as pd
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Show appropriate sidebar links 
SideBarLinks()

# Display page title for medical information input 
st.write("Medical Information Input")

# Create a form for entering medical information
with st.form("enter med info"):
    # Input field for the camperID
    c_id = st.text_input("Please input your camper's ID:")
    # Input field for the medical condition ID
    m_id = st.text_input("Pleas input the medical condition's ID (see table below):")
    # Submit button for the form 
    submitted = st.form_submit_button("submit")
    if submitted: 
        # Create a dictionary to store the data
        data = {}
        data["camperID"] = c_id
        data["medID"] = m_id
        # Display the submitted data on the page 
        st.write(data)
        # Send a POST request to the API with the submitted data
        requests.post('http://api:4000/g/guardian', json = data)

# Define the data
data = [
    (1, 'Peanut allergy'),
    (2, 'Tree nut allergy'),
    (3, 'Dairy allergy'),
    (4, 'Egg allergy'),
    (5, 'Soy allergy'),
    (6, 'Wheat allergy'),
    (7, 'Shellfish allergy'),
    (8, 'Fish allergy'),
    (9, 'Gluten free/Celiac disease'),
    (10, 'Sesame allergy'),
    (11, 'Corn allergy'),
    (12, 'Mustard allergy'),
    (13, 'Lactose intolerance'),
    (14, 'Vegan diet'),
    (15, 'Vegetarian diet'),
    (16, 'Halal diet'),
    (17, 'Kosher diet'),
    (18, 'Low-sodium diet'),
    (19, 'Low-sugar/Diabetic diet'),
    (20, 'High-protein diet'),
    (21, 'FODMAP diet'),
    (22, 'Keto diet'),
    (23, 'Nut-free diet'),
    (24, 'Asthma'),
    (25, 'Type 1 Diabetes'),
    (26, 'Epilepsy'),
    (27, 'ADHD'),
    (28, 'Autism Spectrum Disorder (ASD)'),
    (29, 'Anxiety disorders'),
    (30, 'Depression'),
    (31, 'Cerebral palsy'),
    (32, 'Down syndrome'),
    (33, 'Hemophilia'),
    (34, 'Juvenile rheumatoid arthritis'),
    (35, 'Congenital heart defects'),
    (36, 'Cystic fibrosis'),
    (37, 'Sickle cell anemia'),
    (38, 'Eczema'),
    (39, 'FPIES'),
    (40, 'Migraines')
]

# Create a DataFrame
df = pd.DataFrame(data, columns=['Medican Condition ID', 'Medical Condition'])

# Streamlit app
st.title('Medical ID Reference Table')

# Display the table
st.dataframe(df, hide_index=True)

