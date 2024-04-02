# streamlit run c:\Users\DICCE\Desktop\sw_project_music_app\home.py

# Import
import streamlit as st

# 제목
with st.container():
    st.title('Music Composer App', anchor=False)
    st.subheader('The easiest way to be a composer!', anchor=False)

with st.container():
    st.link_button('Try Now', 'pages/app.py', use_container_width=True)