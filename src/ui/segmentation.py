import streamlit as st
from src.core.segmentation import *

def run_module(image):
    operation = st.selectbox(
        "Choose Operation",
        [
            "None",
            "Outlier Removal",
            "Gaussian Smoothing",
            "Global Thresholding",
            "Automatic Thresholding",
            "Adaptive Thresholding"
        ]
    )

    if operation == "Outlier Removal":
        result = outlier_removal(image)
        st.image(result, channels="BGR")

    elif operation == "Gaussian Smoothing":
        ksize = st.slider("Kernel Size", 3, 21, 5, step=2)
        result = gaussian_smoothing(image, ksize)
        st.image(result, channels="BGR")

    elif operation == "Global Thresholding":
        thresh_val = st.slider("Threshold Value", 0, 255, 127)
        result = global_threshold(image, thresh_val)
        st.image(result)

    elif operation == "Automatic Thresholding":
        result = automatic_threshold(image)
        st.image(result)

    elif operation == "Adaptive Thresholding":
        result = adaptive_threshold(image)
        st.image(result)

    else:
        st.info("Select an operation")