import streamlit as st

def show_images(img, new_img, channels=''):
    col_input, col_output = st.columns(2)
    with col_input:
        st.subheader("Original Image")
        st.image(img, channels="BGR", width="stretch")
        
    with col_output:
        st.subheader("Output Image")
        st.image(new_img, channels=channels)