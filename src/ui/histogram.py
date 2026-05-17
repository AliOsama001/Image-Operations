import streamlit as st
from src.core import histogram

def run_module(image):
    operation = st.selectbox(
        "Histogram Operation",
        ["None", "Histogram Stretching", "Histogram Equalization"]
    )
    
    if len(image.shape) == 3:
        display_channels = "BGR"
    else:
        display_channels = "RGB"

    if operation == "Histogram Stretching":
        result = histogram.histogram_stretching(image)
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels=display_channels)

    elif operation == "Histogram Equalization":
        result = histogram.histogram_equalization(image)
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels=display_channels)

    else:
        st.info("Select histogram operation")