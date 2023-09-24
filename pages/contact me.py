import pandas as pd
import streamlit as st
from functions import send_email
import pandas as pd

tps=pd.read_csv('pages/tps.csv')
st.subheader("Contact me!")
st.write("Enter the below details, I will get back at earliest!")

with st.form(key="forms"):
    email = st.text_input("Enter your email:")
    category = st.selectbox("Choose Category", tps['topics'])
    msg = st.text_area("Write your message:")
    button = st.form_submit_button("submit")
    message = f"""\
Subject: New email from {email}

from: {email}
category:{category}
message:{msg}"""

    if button:
        send_email(message)
        st.info("Your email was sent successfully!")




#     write("Your Name:")
# st.text_input(label='', key="name")
#
# st.write("Drop your email id:")
# st.text_input(label='', key="email")
#
# st.write("Buddy, Type me a message!")
# st.text_input(label='', key="msg")