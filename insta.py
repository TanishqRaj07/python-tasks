import streamlit as st
import requests

def instagram_ui():
    st.header("\ud83d\udcf8 Instagram Post (Business Account)")
    token = st.text_input("Access Token", type="password")
    page_id = st.text_input("Instagram Page ID")
    image_url = st.text_input("Image URL (public)")
    caption = st.text_area("Caption")

    if st.button("Post to Instagram"):
        try:
            res1 = requests.post(
                f"https://graph.facebook.com/v19.0/{page_id}/media",
                data={"image_url": image_url, "caption": caption, "access_token": token}
            ).json()
            creation_id = res1.get("id")
            if creation_id:
                res2 = requests.post(
                    f"https://graph.facebook.com/v19.0/{page_id}/media_publish",
                    data={"creation_id": creation_id, "access_token": token}
                ).json()
                if "id" in res2:
                    st.success("\u2705 Instagram post published!")
                else:
                    st.error(res2)
            else:
                st.error(res1)
        except Exception as e:
            st.error(str(e))
