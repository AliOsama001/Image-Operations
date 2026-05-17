import streamlit as st
from src.core import mathematical_morphology

def run_module(image):
    operation = st.selectbox(
        "Morphology Operations",
        ["None", "Dilation", "Erosion", "Opening"]
    )

    k = st.slider("Kernel Size", 3, 11, 3, step=2)

    if operation == "Dilation":
        st.image(mathematical_morphology.dilation(image, k), channels="BGR")

    elif operation == "Erosion":
        st.image(mathematical_morphology.erosion(image, k), channels="BGR")

    elif operation == "Opening":
        st.image(mathematical_morphology.opening(image, k), channels="BGR")

    else:
        st.info("Select Morphology operation")