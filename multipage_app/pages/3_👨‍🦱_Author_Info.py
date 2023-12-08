from PIL import Image
import streamlit as st

st.set_page_config(page_title='Multipage App', page_icon='🤖', layout='wide')

myphoto = Image.open('images/myinfo.jpg')

with st.container():
    st.title('My Information')

with st.container():
    left_column, right_column = st.columns((1, 2))
    with left_column:
        st.image(myphoto)
    with right_column:
        st.subheader('Nic Albert B. Seraño')
        st.subheader('BSCpE 1B')
        st.subheader('[Facebook link...](https://www.facebook.com/beeboy.sirrunyou)')




