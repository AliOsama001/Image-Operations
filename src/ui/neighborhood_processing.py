import streamlit as st
from src.core import neighborhood_processing
from src.utils import show_images

def run_module(image):
    operation = st.selectbox("Choose Filter Type",["None","Average Filter","Laplacian Filter","Median Filter","Max Filter","Min Filter"])
    ksize = st.slider("Kernel Size", 3, 11, 3, step=2)

    if operation == "Average Filter":
        result = neighborhood_processing.average_filter(image, ksize)
        show_images(image, result, "BGR")

    elif operation == "Laplacian Filter":
        result = neighborhood_processing.laplacian_filter(image)
        show_images(image, result, "BGR")

    elif operation == "Median Filter":
        result = neighborhood_processing.median_filter(image, ksize)
        show_images(image, result, "BGR")

    elif operation == "Max Filter":
        result = neighborhood_processing.max_filter(image, ksize)
        show_images(image, result, "BGR")

    elif operation == "Min Filter":
        result = neighborhood_processing.min_filter(image, ksize)
        show_images(image, result, "BGR")

    else:
        st.info("Select operation")