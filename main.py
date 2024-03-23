import streamlit as st
import winsound

if st.button('Say hello'):
    winsound.Beep(523, 500)