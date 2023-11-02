import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo_me.png")

with col2:
    st.title("David Mundy")
    blurb="""
    Hi, I am David! I am currently an IT Manager looking to tranistion into a DevOps role. 
    
    I have over 15 years of experience in a wide range of organisations 
    including public, private and charity sectors. A passion for tech and a keen interest in transitioning to a cloud engineering position.
    """
    st.info(blurb)

subtitle = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(subtitle)

col3, spacer_col1, col4 = st.columns([1.5,0.5,1.5])


df = pandas.read_csv("data.csv", sep=";")


with col3:
    for index, row in df[:2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Github]({row['url']})")

with col4:
    for index, row in df[2:4].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Github]({row['url']})")
