import streamlit as st

# Page configuration
st.set_page_config(page_title="Happy Mother's Day!", layout="centered")

# Background gradient
page_bg_img = '''
<style>
body {
    background: linear-gradient(120deg, #fbc2eb 0%, #a6c1ee 100%);
    font-family: "Comic Sans MS", cursive, sans-serif;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title
st.markdown("""
    <h1 style='text-align: center; color: #e84393; font-size: 50px;'>
        💐 Happy Mother's Day 💐
    </h1>
""", unsafe_allow_html=True)

message = """
<div style='text-align: center; font-size: 24px; color: #ffffff; margin-top: 20px;
             text-shadow: 1px 1px 2px rgba(255,255,255,0.7);'>
    <p>To the most wonderful mother and wife,</p>
    <p>Your kindness and love are the light of our life.</p>
    <p>With every hug and every smile,</p>
    <p>You make our world worthwhile 💖</p>
</div>
"""
st.markdown(message, unsafe_allow_html=True)

# New wholesome animation (sparkling hearts)
st.image("https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif", caption="You're loved more than words can say 💞", use_container_width=True)

# Footer
st.markdown("<hr style='border: 1px solid #e84393;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6c5ce7;'>Made with ❤️ just for you!</p>", unsafe_allow_html=True)
