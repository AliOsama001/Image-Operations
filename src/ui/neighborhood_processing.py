import streamlit as st
from src.core import neighborhood_processing

def run_module(image):
    operation = st.selectbox("Choose Filter Type",["None","Average Filter","Laplacian Filter","Median Filter","Max Filter","Min Filter"])
    ksize = st.slider("Kernel Size", 3, 11, 3, step=2)

    if operation == "Average Filter":
        result = neighborhood_processing.average_filter(image, ksize)
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    elif operation == "Laplacian Filter":
        result = neighborhood_processing.laplacian_filter(image)
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="GRAY")

    elif operation == "Median Filter":
        result = neighborhood_processing.median_filter(image, ksize)
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    elif operation == "Max Filter":
        result = neighborhood_processing.max_filter(image, ksize)
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    elif operation == "Min Filter":
        result = neighborhood_processing.min_filter(image, ksize)
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")
    else:
        st.info("Select operation")