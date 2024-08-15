import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    Welcome to SummerSync!
SummerSync is your all-in-one solution for streamlined summer camp management. We understand that running a summer camp involves juggling countless details, from camper registrations to activity schedules. Our application is designed to simplify these processes, allowing camp administrators, staff, and families to focus on what truly matters - creating unforgettable summer experiences.
Our Mission
At SummerSync, we aim to revolutionize summer camp operations by providing a comprehensive, user-friendly platform that addresses the unique needs of sleepaway camps and short-term programs alike. Our scalable application adapts to camps of all sizes, ensuring that every aspect of camp life is organized, accessible, and secure.
Key Features
Centralized Information Management
Store and access vital camper and staff information, including contact details, medical records, and certifications, all in one secure location.
Dynamic Scheduling
Effortlessly organize camp activities, assign counselors, and manage cabin placements with our intuitive scheduling tools.
Enhanced Communication
Facilitate seamless communication between camp staff, campers, and families through our integrated messaging system.
Health and Safety
Empower health services with tools to manage allergies, medications, and medical conditions. 
Who Benefits?
Camp Administrators: Gain a bird's-eye view of camp operations and streamline administrative tasks.
Counselors: Access camper information and log incident reports with ease.
Health Services: Efficiently manage camper health needs and track medical information.
Parents/Guardians: Stay connected with their campers, manage billing, and receive camp updates.
Our Commitment
SummerSync is more than just software; it's a commitment to enhancing the summer camp experience for everyone involved. By reducing administrative burdens, we enable camp staff to dedicate more time to creating magical moments and fostering personal growth for campers.
Join us in revolutionizing summer camp management. With SummerSync, you'll have more time to focus on what truly matters - nurturing the next generation of leaders, adventurers, and lifelong friends.
Experience the SummerSync difference today and transform your camp management for a brighter, more organized tomorrow.

    """
        )