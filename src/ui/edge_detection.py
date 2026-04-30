import cv2
import numpy as np
import streamlit as st
from src.core import edge_detection
def run_module(image):

    operation = st.selectbox("Edge Detection",["None", "Sobel"])

    if operation == "Sobel":
        st.image(edge_detection.sobel_edge(image), channels="GRAY")

    else:
        st.info("Select edge method")