import streamlit as st
from twilio.rest import Client

def whatsapp_ui():
    st.header("\ud83d\udeb8\ufe0f WhatsApp Message via Twilio")
    sid = st.text_input("Twilio SID")
    token = st.text_input("Twilio Token", type="password")
    from_num = st.text_input("From (e.g. whatsapp:+1415XXX)")
    to_num = st.text_input("To (e.g. whatsapp:+91XXXXXXXXXX)")
    msg = st.text_area("Message")

    if st.button("Send WhatsApp"):
        try:
            client = Client(sid, token)
            message = client.messages.create(body=msg, from_=from_num, to=to_num)
            st.success(f"\u2705 WhatsApp sent! SID: {message.sid}")
        except Exception as e:
            st.error(str(e))
