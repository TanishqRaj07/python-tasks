import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def email_ui():
    st.header("\ud83d\udce7 Send Email")
    sender_email = st.text_input("Your Email")
    sender_password = st.text_input("App Password", type="password")
    receiver_email = st.text_input("Recipient Email")
    subject = st.text_input("Subject")
    body = st.text_area("Message")

    if st.button("Send Email"):
        try:
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = receiver_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.quit()

            st.success("\u2705 Email sent!")
        except Exception as e:
            st.error(f"\u274c Email failed: {str(e)}")