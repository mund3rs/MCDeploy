import streamlit as st


st.header("Minecraft Server Deployer Development Roadmap")

updates = """
-> Select between different game types e.g. survival, adventure, creative

-> Persist world data to S3 upon instance termination

-> Allow user to enter world seed
"""
st.subheader("A list of all features to come in the future")
st.divider()
st.write(updates)


