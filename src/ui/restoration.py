import streamlit as st
from src.core import image_restoration
from src.utils import show_images

def run_module(image):
    operation = st.selectbox(
        "Restoration / Boundary",
        [
            "None",
            "Internal Boundary",
            "External Boundary",
            "Morphological Gradient"
        ]
    )

    k = st.slider("Kernel Size", 3, 11, 3, step=2)

    if operation == "Internal Boundary":
        result = image_restoration.internal_boundary(image, k)
        show_images(image, result, "BGR")

    elif operation == "External Boundary":
        result = image_restoration.external_boundary(image, k)
        show_images(image, result, "BGR")

    elif operation == "Morphological Gradient":
        result = image_restoration.morphological_gradient(image, k)
        show_images(image, result, "BGR")

    else:
        st.info("Select operation")