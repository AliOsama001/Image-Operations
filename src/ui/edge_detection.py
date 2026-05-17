import streamlit as st
from src.core import edge_detection

def run_module(image):
    operation = st.selectbox("Edge Detection",["None", "Sobel"])

    if operation == "Sobel":
        result = edge_detection.sobel_edge(image)
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="GRAY")

    else:
        st.info("Select edge method")