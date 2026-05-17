import streamlit as st
from src.core import histogram
from src.utils import show_images

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
        show_images(image, result, display_channels)

    elif operation == "Histogram Equalization":
        result = histogram.histogram_equalization(image)
        show_images(image, result, display_channels)

    else:
        st.info("Select histogram operation")