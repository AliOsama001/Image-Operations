import streamlit as st
from src.core import mathematical_morphology

def run_module(image):
    operation = st.selectbox(
        "Morphology Operations",
        ["None", "Dilation", "Erosion", "Opening"]
    )

    k = st.slider("Kernel Size", 3, 11, 3, step=2)

    if operation == "Dilation":
        result = mathematical_morphology.dilation(image, k)
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    elif operation == "Erosion":
        result = mathematical_morphology.erosion(image, k)
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    elif operation == "Opening":
        result = mathematical_morphology.opening(image, k)
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    else:
        st.info("Select Morphology operation")