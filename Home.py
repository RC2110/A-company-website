import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.header("TheAIPlace")
content="""Microsoft is a global developer and licensor of software, devices, solutions, and services. 
The company is well known for its Windows and Office Suite software but nets a growing share of its profit and revenue from cloud computing and its cloud platform, Azure. 
Microsoft also owns and operates LinkedIn, the popular social networking site for job seekers."""
st.write(content)
st.subheader("Our Team")

content = pd.read_csv("data.csv")

col1,col2,col3 = st.columns(3)

with col1:
    for index, row in content[:4].iterrows():
        st.subheader(row['first name'].title() + ' ' + row['last name'].title())
        st.write(row['role'])
        st.image('Images/' + f"{row['image']}")

with col2:
    for index, row in content[4:8].iterrows():
        st.subheader(row['first name'].title() + ' ' + row['last name'].title())
        st.write(row['role'])
        st.image("Images/" + f"{row['image']}")

with col3:
    for index, row in content[8:].iterrows():
        st.subheader(row['first name'].title() + ' ' + row['last name'].title())
        st.write(row['role'])
        st.image("Images/" + f"{row['image']}")