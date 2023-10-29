import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1,col_spacer,col2 = st.columns([0.5,0.5,1.5])

with col1:
    st.image("images/MC-Logo.png")

with col2:
    st.title("Minecraft Server Deployer")
    blurb="""
    Click the button to deploy a minecraft server. Email address is required to recieve IP address.
    """
    st.info(blurb)

    email = st.text_input("Email", "", placeholder="Enter email address")
    
st.divider()

subtitle = """
Please submit feedback on the left. Thanks!
"""

st.write(subtitle)
