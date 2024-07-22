import streamlit as st
st.set_page_config(page_title="Gaji seorang Software Developer", page_icon="800px-Stack_Overflow_icon.svg.png")

from predict_page import show_predict_page
from explore_page import show_explore_page

with open ('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
page = st.sidebar.selectbox("Mengeksplora atau Memprediksi", ("Memprediksi", "Mengeksplora"))

if page == "Memprediksi":
    show_predict_page()
else:
    show_explore_page()