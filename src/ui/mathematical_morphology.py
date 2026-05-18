import streamlit as st
from src.core import mathematical_morphology
from src.utils import show_images

def run_module(image):
    operation = st.selectbox(
        "Morphology Operations",
        ["None", "Dilation", "Erosion", "Opening", "Internal Boundary", "External Boundary", "Morphological Gradient"]
    )

    k = st.slider("Kernel Size", 3, 11, 3, step=2)

    if operation == "Dilation":
        result = mathematical_morphology.dilation(image, k)
        show_images(image, result, "BGR")

    elif operation == "Erosion":
        result = mathematical_morphology.erosion(image, k)
        show_images(image, result, "BGR")

    elif operation == "Opening":
        result = mathematical_morphology.opening(image, k)
        show_images(image, result, "BGR")

    elif operation == "Internal Boundary":
        result = mathematical_morphology.internal_boundary(image, k)
        show_images(image, result, "BGR")

    elif operation == "External Boundary":
        result = mathematical_morphology.external_boundary(image, k)
        show_images(image, result, "BGR")

    elif operation == "Morphological Gradient":
        result = mathematical_morphology.morphological_gradient(image, k)
        show_images(image, result, "BGR")

    else:
        st.info("Select Morphology operation")