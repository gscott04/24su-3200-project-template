# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')

def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ Guardian Role ------------------------
def GuardianHomeNav():
    st.sidebar.page_link("pages/40_Guardian_Home.py", label="Guardian Home", icon='👤')

def GuardianTestNav():
    st.sidebar.page_link("pages/41_Guardian_Test.py", label="Test the Guardian API", icon='🛜')

def GuardianScheduleNav():
    st.sidebar.page_link("pages/42_Guardian_DailySchedule.py", label="Check Daily Schedule", icon='🗓️')

def GuardianContactNav():
    st.sidebar.page_link("pages/43_Guardian_contact.py", label="Get your child's counselor's contact info", icon='📲')
    
#### ------------------------ Camp Counselor Role ------------------------
def CampCounselorHomeNav():
    st.sidebar.page_link("pages/50_Camp_Counselor_Home.py", label="Camp Counselor Home", icon='👤')

def CampCounselorStaff():
    st.sidebar.page_link("pages/51_Camp_Counselor_Staff_Info.py", label="Camp Counselor find staff", icon='👤')

def CampCounselorStaff():
    st.sidebar.page_link("pages/52_Camp_Counselor_Delete.py", label="Camp Counselor delete", icon='👤')

def CampCounselorStaff():
    st.sidebar.page_link("pages/53_Camp_Counselor_Update_Activity.py", label="Camp Counselor activity change", icon='👤')

#### ------------------------ Camp Director Role ------------------------
def CampDirectorHomeNav():
    st.sidebar.page_link("pages/60_Camp_Director_Home.py", label="Camp Director Home", icon='👤')

def CampDirectorCabinInfo():
    st.sidebar.page_link("pages/61_Camp_Director_Cabin_Info.py", label="Camp Director Information", icon='👤')    

def CampDirectorGuardianInfo():
    st.sidebar.page_link("pages/62_Camp_Director_Guardian_Info.py", label="Guardian Information", icon='👤')  

#### ------------------------ App Admin Role ------------------------
def AppAdminHomeNav():
    st.sidebar.page_link("pages/70_App_Admin_Home.py", label="App Admin Home", icon='👤')

def AppAdminDirectorNav():
    st.sidebar.page_link("pages/71_App_Admin_DirectorID.py", label="App Admin Director ID", icon='👤')

def AppAdminCampNav():
    st.sidebar.page_link("pages/72_App_Admin_Contact.py", label="App Admin Outreach", icon='🧑‍💻')

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
            GuardianTestNav()
            GuardianScheduleNav()
            GuardianContactNav()
            
        if st.session_state['role'] == 'camp_counselor':
            CampCounselorHomeNav()      

        if st.session_state['role'] == 'camp_director':
            CampDirectorHomeNav()  
            CampDirectorCabinInfo()
            CampDirectorGuardianInfo()

        if st.session_state['role'] == 'app_admin':
            AppAdminHomeNav()   
            AppAdminDirectorNav() 
            AppAdminCampNav()      


    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('Home.py')

