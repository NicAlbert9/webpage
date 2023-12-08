import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title='Multipage App',
    page_icon='🤖',
    layout='wide',
)

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

my_animation = load_lottieurl('https://lottie.host/7699240a-4a1c-4e13-b7bb-42eefbd42602/tcMrWugvsB.json')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css.txt")

with st.container():
    st.header('Get in Touch with me!')
    st.write('##')

    contact_form = """
    <form action="https://formsubmit.co/beboyimba30@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email"placeholder="Your email" required>
     <textarea name="message" placeholder="Your message" required></textarea>
     <button type="submit">Send</button>
</form>
"""
    left_column, right_column = st.columns((2,2))
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(my_animation, height = 350, key = 'coding')
