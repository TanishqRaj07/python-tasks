import streamlit as st
import requests
import json

def linkedin_ui():
    st.header("\ud83d\udd17 LinkedIn Post")
    token = st.text_input("LinkedIn Access Token", type="password")
    content = st.text_area("Post Content")
    if st.button("Post to LinkedIn"):
        try:
            headers = {"Authorization": f"Bearer {token}"}
            user_id = requests.get("https://api.linkedin.com/v2/me", headers=headers).json()["id"]

            post_url = "https://api.linkedin.com/v2/ugcPosts"
            post_data = {
                "author": f"urn:li:person:{user_id}",
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {"text": content},
                        "shareMediaCategory": "NONE"
                    }
                },
                "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
            }

            res = requests.post(post_url, headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "X-Restli-Protocol-Version": "2.0.0"
            }, data=json.dumps(post_data))

            if res.status_code == 201:
                st.success("\u2705 LinkedIn post successful!")
            else:
                st.error(res.text)
        except Exception as e:
            st.error(str(e))
