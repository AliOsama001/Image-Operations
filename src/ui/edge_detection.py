import streamlit as st
from src.core import edge_detection
from src.utils import show_images

def run_module(image):
    operation = st.selectbox("Edge Detection",["None", "Sobel"])

    if operation == "Sobel":
        result = edge_detection.sobel_edge(image)
        show_images(image, result, "GRAY")

    else:
        st.info("Select edge method")