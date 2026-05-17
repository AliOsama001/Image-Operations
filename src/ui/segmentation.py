import streamlit as st
from src.core import segmentation
from src.utils import show_images

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
        result = segmentation.outlier_removal(image)
        show_images(image, result, "BGR")

    elif operation == "Gaussian Smoothing":
        ksize = st.slider("Kernel Size", 3, 21, 5, step=2)
        result = segmentation.gaussian_smoothing(image, ksize)
        show_images(image, result, "BGR")

    elif operation == "Global Thresholding":
        thresh_val = st.slider("Threshold Value", 0, 255, 127)
        result = segmentation.global_threshold(image, thresh_val)
        show_images(image, result)

    elif operation == "Automatic Thresholding":
        result = segmentation.automatic_threshold(image)
        show_images(image, result)

    elif operation == "Adaptive Thresholding":
        result = segmentation.adaptive_threshold(image)
        show_images(image, result)

    else:
        st.info("Select an operation")