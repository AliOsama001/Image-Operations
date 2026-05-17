import streamlit as st
from src.core import color_ops

def run_module(image):
    operation = st.selectbox(
        "Color Operations", 
        ["None", "Change Red", "Swap Channels", "Remove Channel"]
    )

    if operation == "Change Red":
        value = st.slider("Red Intensity", -255, 255, 0)
        result = color_ops.change_red(image, value)
        
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
            
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    elif operation == "Swap Channels":
        result = color_ops.swap_channels(image)
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    elif operation == "Remove Channel":
        channel = st.selectbox("Select Channel", ["Red", "Green", "Blue"])
        result = color_ops.remove_channel(image, channel)
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    else:
        st.info("Select Color operation")