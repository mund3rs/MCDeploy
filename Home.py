import streamlit as st
from start_ec2 import start_ec2

st.set_page_config(layout="wide")

colSpacer1, col1, colSpacer2 = st.columns([1,1,1])

with col1:
    st.header("Deploy a Minecraft Server")
    st.image("images/MC-Logo.png", width=250)


colSpacer3, col2, colSpacer4 = st.columns([0.5,1.5,0.5])

with col2:
    st.title("")
    blurb="""
    Hey! Looking for a small private Minecraft server? You're in the right place. Select from the options below. 
    The servers provisioned are suitable for up to 6 players. They are hosted on AWS EC2 instances and are terminated after you've finished.
    The options are: Vanilla, ##### or #####. Worlds are not persisted (although I'm working on that).
    """
    st.write(blurb)
    subtitle = """
    To see what plans there are for this app click the roadmap link on the left or use the contact form to submit feedback.
    """
    st.info(subtitle)

colSpacer5, col3, colSpacer6 = st.columns([0.5,1.5,0.5])

with col3:
    with st.form(key="mc_deploy"):
        user_email = st.text_input("Your email address")
        col4, col5, col6 = st.columns([1.0,1.0,1.0])
        with col4:
            button1 = st.form_submit_button("Vanilla", use_container_width=True)
        with col5:
            button2 = st.form_submit_button("Coming Soon", use_container_width=True, disabled=True)
        with col6:
            button3 = st.form_submit_button("Coming Soon 2", use_container_width=True, disabled=True)
        if button1:
            serverType = 'vanilla'
            start_ec2(user_email, serverType)
            st.info("Vanilla Server Deploying - you will be sent the IP shortly")
        elif button2:
            serverType = 'type2'
            start_ec2(user_email, serverType)
            st.info("Type 2 Deploying")
        elif button3:
            serverType = 'type3'
            start_ec2(user_email, serverType)
            st.info("Type 3 Deploying")






