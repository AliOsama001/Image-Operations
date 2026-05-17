import streamlit as st
from src.core import image_restoration

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
        st.image(image_restoration.internal_boundary(image, k), channels="BGR")

    elif operation == "External Boundary":
        st.image(image_restoration.external_boundary(image, k), channels="BGR")

    elif operation == "Morphological Gradient":
        st.image(image_restoration.morphological_gradient(image, k), channels="BGR")

    else:
        st.info("Select operation")