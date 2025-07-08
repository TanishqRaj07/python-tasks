import streamlit as st
import requests

def facebook_ui():
    st.header("\ud83d\udcbc Facebook Page Post")
    token = st.text_input("Page Access Token", type="password")
    page_id = st.text_input("Page ID")
    msg = st.text_area("Message")

    if st.button("Post to Facebook"):
        try:
            url = f"https://graph.facebook.com/{page_id}/feed"
            res = requests.post(url, params={"message": msg, "access_token": token}).json()
            if "id" in res:
                st.success("\u2705 Post ID: " + res["id"])
            else:
                st.error(str(res))
        except Exception as e:
            st.error(str(e))
