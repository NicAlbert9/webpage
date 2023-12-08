import streamlit as st

st.set_page_config(
    page_title='Multipage App',
    page_icon='🤖',
    layout='wide',
)

st.sidebar.success('Select page above.')


with st.container():
    left_column, center_column, right_column = st.columns((1.3, 2, 1.3))
    with center_column:
        st.title('◀ Welcome to my Webpage ▶')


with st.container():
    st.write('---')
    left_column1, right_column1 = st.columns((0.8, 2))

    with right_column1:
        st.header('Programming Project')
    with left_column1:
        st.empty()

    with st.container():
        left_column2, right_column2 = st.columns((0.5, 2))
    with right_column2:
      st.write('####')
      st.write('Make Webpage using Streamlit')
      st.write('Then Host your [Streamlit](https://streamlit.io/) app on [Github](https://github.com/)')
      st.write('[Click Here for Tutorial](https://blog.streamlit.io/host-your-streamlit-app-for-free/)')
    with left_column2:
        st.empty()
