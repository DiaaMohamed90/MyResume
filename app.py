from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "prof.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Diaa Mohamed"
PAGE_ICON = ":wave:"
NAME = "Diaa Mohamed"
DESCRIPTION = """
IT Manager
"""
EMAIL = "Diaamohamed23@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/diaa-mohamed-56b886151/",
    "GitHub": "https://github.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (GUI Applications(TKINTER), Pandas , Automation(SELENIUM,HELIUM), Webscrapping)
- 🗄️ Databases: Sqlite3, SQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**IT Manager| Professional Ready Mix **")
st.write("01/2020 - Present")
st.write(
    """
- ► Design and configure all the network equipments and security for head office and three
    other branches.
- ► Perform day-to-day administration of the company's network infrastructure.
- ► Monitor and troubleshoot network performance and security issues.
- ► Recommended procedure modifications or improvements.
- ► Creating rational strategies for upgrading the company network software whenever a new
    update is available.
- ► Constructing and implementing plans to ensure the company network continues to operate
    smoothly in the event of a problem.
- ► Train and provide troubleshooting procedures to helpdesk personnel for first-line network
    issues.

- ► Establishing networking environment by designing system configuration, directing system
    installation, defining, documenting, and enforcing system standards.
- ► Securing network system by establishing and enforcing policies, and defining and
    monitoring access.
- ► Managing and maintaining the file server.
- ► Install new CCTV system for the head office and the other three branches
- ► Implementation of ERP system (BRIGHT INFORMATION SYSTEM) For Head Office and other
    three branches.
- ► Design And Build GUI Appraisal Form Application for HR Department using (python) each
    manager in our company can evaluate his employees and the results Automatically Sent to HR
    Manager by Email
- ►  Design And Build a Small HR System Contains (employee data & Vacations & Attendance &
    Salaries).

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**SYSTEM ADMINISTRATOR | PACK TEC COMPANY.**")

st.write(
    """
- ► Properly escalate unresolved queries to the next level of support.
- ► Securing network system by establishing and enforcing policies, and defining and
    monitoring access.
- ► Maintain and troubleshoot district network based services: File and Print services, Email, Active
    Directory and DHCP/DNS.
- ► Configure, maintain, monitor, and troubleshoot windows software Deployments.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**NETWORK AND SYSTEM ADMINISTRATOR | GOODSMART(FREELANCE)**")

st.write(
    """
- ► Design and configure all the network equipments and security
- ► Install, maintain, upgrade, and troubleshoot routers, gateways, firewalls, and other
    networking infrastructure for local area and wide area networks (LAN/WAN), including
    Internet connectivity.
- ► Implementation of open source Firewall(Clear Os)
"""
)
# --- Job 4 
st.write('\n')
st.write("🚧","**NETWORK AND SYSTEM ADMINISTRATOR | EAGLES CAR (FREELANCE)**")
st.write(
    """
- ► Design and configure all the network equipments and security
- ► Install, maintain, upgrade, and troubleshoot routers, gateways, firewalls, and other
    networking infrastructure for local area and wide area networks (LAN/WAN), including
    Internet connectivity.
- ► Implementation OF A NEW CCTV SYSTEM FOR THE Company.
"""
)

## - Job 5 

st.write('\n')
st.write("🚧","**NETWORK AND SYSTEM ADMINISTRATOR | MASS Packing AND FOOD PROCESSING (FREELANCE)**")
st.write(
    """
- ► Design and configure all the network equipments and security
- ► Install, maintain, upgrade, and troubleshoot routers, gateways, firewalls, and other
    networking infrastructure for local area and wide area networks (LAN/WAN), including
    Internet connectivity.
- ► Implementation OF A NEW CCTV SYSTEM FOR THE Company.
"""
)

## - job 6 
st.write('\n')
st.write("🚧","**Help Desk | Bedaya INTERNATIONAL SCHOOL **")
st.write(
    """
- ► Serve As The First Point OF Contact For Seeking Technical Assistance.
- ► Installing And Configuring Software, hardware and networks.
- ► Provide troubleshooting and configuration support for client desktop and networking environment.
- ► Create New User accounts.
"""
)
## - job 7 
st.write('\n')
st.write("🚧","**SITE Engineer | NEC Company **")


st.write('\n')
st.write("🚧","**MILITARY OFFICER AT THE ARMED FORCES. | FROM June 2014 To October 2017 **")
# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
