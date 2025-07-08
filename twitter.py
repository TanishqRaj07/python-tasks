import streamlit as st
import tweepy

def twitter_ui():
    st.header("\ud83d\udd4a\ufe0f Twitter Post")
    key = st.text_input("API Key")
    secret = st.text_input("API Secret", type="password")
    token = st.text_input("Access Token")
    token_secret = st.text_input("Access Token Secret", type="password")
    tweet = st.text_area("Tweet")

    if st.button("Post Tweet"):
        try:
            auth = tweepy.OAuth1UserHandler(key, secret, token, token_secret)
            api = tweepy.API(auth)
            api.update_status(tweet)
            st.success("\u2705 Tweet posted!")
        except Exception as e:
            st.error(str(e))
