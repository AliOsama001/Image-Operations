import streamlit as st
from src.core import image_restoration  
import cv2
import numpy as np
from src.utils import show_images

def run_module(image):
    operation = st.selectbox(
        "Restoration Operations",
        ["None", "average_filter", "Median Filter", "laplacian_filter", "Outlier Method", "Image Averaging"]
    )

    if operation == "average_filter":
        ksize = st.slider("Kernel Size", 3, 11, 3, step=2)
        result = image_restoration.average_filter(image, ksize)
        show_images(image, result, "BGR")

    elif operation == "Median Filter":
        ksize = st.slider("Kernel Size", 3, 11, 3, step=2)
        result = image_restoration.median_filter(image, ksize)
        show_images(image, result, "BGR")

    elif operation == "laplacian_filter":
        ksize = st.slider("Kernel Size", 3, 11, 3, step=2)
        sigma = st.slider("Sigma (Standard Deviation)", 0.1, 10.0, 1.0, step=0.1)
        result = image_restoration.laplacian_filter(image, ksize, sigma)
        show_images(image, result, "BGR")

    elif operation == "Outlier Method":
        threshold = st.slider("Outlier Threshold ", 10, 100, 30)
        result = image_restoration.outlier_method(image, threshold)
        show_images(image, result, "BGR")   

    else:
        st.info("Select Restoration operation")