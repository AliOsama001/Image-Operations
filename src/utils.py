import streamlit as st
import cv2

def show_images(old_img, new_img, channels):
    col_input, col_output = st.columns(2)
    with col_input:
        st.subheader("Original Image")
        st.image(old_img, channels="BGR", use_container_width=True)
        
    with col_output:
        st.subheader("Output Image")
        st.image(new_img, channels=channels, use_container_width=True)
        
        success, buffer = cv2.imencode('.png', new_img)
        byte_im = buffer.tobytes()
        
        st.write("")
        st.download_button(
            label=" Download Output Image",
            data=byte_im,
            file_name="processed_image.png",
            mime="image/png"
        )