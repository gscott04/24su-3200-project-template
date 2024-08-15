import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks(show_home=True)

st.title("Welcome to SummerSync!")
st.divider()
st.subheader("Lovingly made by the Data Dwellers at Northeastern during Summmer 2 in 2024.", divider="green")
st.text("""SummerSync is your all-in-one solution for streamlined summer camp management. 
We understand that running a summer camp involves juggling countless details, 
from camper registrations to activity schedules. Our application is designed 
to simplify these processes, allowing camp administrators, staff, and families 
to focus on what truly matters - creating unforgettable summer experiences.""");
st.divider()

st.header("Our Mission", divider="green")
st.text("""At SummerSync, we aim to revolutionize summer camp operations by providing a 
comprehensive, user-friendly platform that addresses the unique needs of sleepaway 
camps and short-term programs alike. Our scalable application adapts to camps 
of all sizes, ensuring that every aspect of camp life is organized, accessible, 
and secure.""")
st.divider()

st.header("Key Features", divider="green")
st.subheader("Centralized Information Management")
st.text("""Store and access vital camper and staff information, including contact details, 
medical records, and certifications, all in one secure location.""")
st.subheader("Dynamic Scheduling")
st.text("""Effortlessly organize camp activities, assign counselors, and manage cabin 
placements with our intuitive scheduling tools.""")
st.subheader("Enhanced Communication")
st.text("""Facilitate seamless communication between camp staff, campers, and families 
through our integrated messaging system.""")
st.subheader("Health and Safety")
st.text("""Empower health services with tools to manage allergies, medications, and 
medical conditions.""")
st.divider()

st.header("Who Benefits?", divider="green")
st.text("""Camp Administrators: Gain a bird's-eye view of camp operations and streamline 
administrative tasks.""")
st.text("Counselors: Access camper information and log incident reports with ease.")
st.text("""Health Services: Efficiently manage camper health needs and track medical 
information.""")
st.text("""Parents/Guardians: Stay connected with their campers, manage billing, and receive 
camp updates.""")
st.divider()

st.header("Our Commitment", divider="green")
st.text("""SummerSync is more than just software; it's a commitment to enhancing the summer 
camp experience for everyone involved. By reducing administrative burdens, we 
enable camp staff to dedicate more time to creating magical moments and fostering 
personal growth for campers.""")
st.text("")
st.text("""Join us in revolutionizing summer camp management. With SummerSync, you'll have more 
time to focus on what truly matters - nurturing the next generation of leaders, 
adventurers, and lifelong friends. Experience the SummerSync difference today and 
transform your camp management for a brighter, more organized tomorrow.""")