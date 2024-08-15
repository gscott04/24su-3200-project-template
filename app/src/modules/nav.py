# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')

def AboutPageNav():
    st.sidebar.page_link("pages/50_About.py", label="About", icon="⛺")

#### ------------------------ Guardian Role ------------------------
def GuardianHomeNav():
    st.sidebar.page_link("pages/10_Guardian_Home.py", label="Guardian Home", icon='🏠')

def GuardianMedNav():
    st.sidebar.page_link("pages/11_Guardian_Med_Post.py", label="Add Child's Medical Needs", icon='💊')

def GuardianScheduleNav():
    st.sidebar.page_link("pages/12_Guardian_Items.py", label="Required Items For a Day", icon='🗓️')

def GuardianContactNav():
    st.sidebar.page_link("pages/13_Guardian_contact.py", label="Counselor's Contact Info", icon='📲')
    
#### ------------------------ Camp Counselor Role ------------------------
def CampCounselorHomeNav():
    st.sidebar.page_link("pages/20_Camp_Counselor_Home.py", label="Camp Counselor Home", icon='🏠')

def CampCounselorStaff():
    st.sidebar.page_link("pages/21_Camp_Counselor_Staff_Info.py", label="Find Your Coworkers", icon='👤')

def CampCounselorDelete():
    st.sidebar.page_link("pages/22_Camp_Counselor_Delete.py", label="Delete an Unplanned Activity", icon='🗑️')

def CampCounselorUpdate():
    st.sidebar.page_link("pages/23_Camp_Counselor_Update_Activity.py", label="Change an Activity Description", icon='🗓️')

#### ------------------------ Camp Director Role ------------------------
def CampDirectorHomeNav():
    st.sidebar.page_link("pages/30_Camp_Director_Home.py", label="Camp Director Home", icon='🏠')

def CampDirectorCabinInfo():
    st.sidebar.page_link("pages/31_Camp_Director_Cabin_Info.py", label="Staff Cabin Look-Up", icon='⛺')    

def CampDirectorGuardianInfo():
    st.sidebar.page_link("pages/32_Camp_Director_Guardian_Info.py", label="Guardian Contact Information", icon='👤')  

def CampDirectorGuardianPaid():
    st.sidebar.page_link("pages/33_Camp_Director_Guardian_Paid.py", label="Guardian Billing Status", icon='💰')      

#### ------------------------ App Admin Role ------------------------
def AppAdminHomeNav():
    st.sidebar.page_link("pages/40_App_Admin_Home.py", label="App Admin Home", icon='🏠')

def AppAdminDirectorNav():
    st.sidebar.page_link("pages/41_App_Admin_DirectorID.py", label="Find Camp Directors", icon='👤')

def AppAdminCampNav():
    st.sidebar.page_link("pages/42_App_Admin_Contact.py", label="Guardian Outreach", icon='📲')

def AppAdminCampContactNav():
    st.sidebar.page_link("pages/43_App_Admin_Camp_Contact.py", label="Camp Outreach", icon='🏕️')

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in. 
    """    

    # add a logo to the sidebar always
    st.sidebar.image("assets/SummerSync.png", width = 260)

    # If there is no logged in user, redirect to the Home (Landing) page
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page('Home.py')
        
    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show Get Daily Schedule, Get Counselor Contact Info, and Update Medical Needs if the user is a guardian.
        if st.session_state['role'] == 'guardian':
            GuardianHomeNav()
            GuardianMedNav()
            GuardianScheduleNav()
            GuardianContactNav()
            
        if st.session_state['role'] == 'camp_counselor':
            CampCounselorHomeNav()    
            CampCounselorStaff()  
            CampCounselorDelete()
            CampCounselorUpdate()

        if st.session_state['role'] == 'camp_director':
            CampDirectorHomeNav()  
            CampDirectorCabinInfo()
            CampDirectorGuardianInfo()
            CampDirectorGuardianPaid()

        if st.session_state['role'] == 'app_admin':
            AppAdminHomeNav()   
            AppAdminDirectorNav() 
            AppAdminCampNav()
            AppAdminCampContactNav()      


    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('Home.py')

