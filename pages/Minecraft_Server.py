import streamlit as st
from start_ec2 import start_ec2


st.header("Minecraft Server Deployer")

st.info("Enter your email address and hit the button to deploy a minecraft server. You'll be sent the public IP of the instance once it's up and running. Enjoy!")

with st.form(key="mc_deploy"):
    user_email = st.text_input("Your email address")
    button = st.form_submit_button("Launch")
    if button:
        start_ec2(user_email)
        st.info("Email sent successfully!")