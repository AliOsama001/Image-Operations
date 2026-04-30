import streamlit as st
import numpy as np
import cv2
from src.core import segmentation
def run_module(image):

    operation = st.selectbox("Choose Filter Type",["None","Average Filter","Laplacian Filter","Median Filter","Max Filter","Min Filter"])
    ksize = st.slider("Kernel Size", 3, 11, 3, step=2)

    if operation == "Average Filter":
        result = segmentation.average_filter(image, ksize)
        st.image(result, channels="BGR")

    elif operation == "Laplacian Filter":
        result = segmentation.laplacian_filter(image)
        st.image(result, channels="GRAY")

    elif operation == "Median Filter":
        result =segmentation.median_filter(image, ksize)
        st.image(result, channels="BGR")

    elif operation == "Max Filter":
        result = segmentation.max_filter(image, ksize)
        st.image(result, channels="BGR")

    elif operation == "Min Filter":
        result = segmentation.min_filter(image, ksize)
        st.image(result, channels="BGR")

    else:
        st.info("Select a filter")