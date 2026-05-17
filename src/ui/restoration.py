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
        result = image_restoration.internal_boundary(image, k)
        
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    elif operation == "External Boundary":
        result = image_restoration.external_boundary(image, k)
        
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    elif operation == "Morphological Gradient":
        result = image_restoration.morphological_gradient(image, k)
        
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    else:
        st.info("Select operation")