import streamlit as st
import cv2
from src.core import histogram
def run_module(image):

    operation = st.selectbox(
        "Histogram Operation",
        ["None", "Histogram Stretching", "Histogram Equalization"]
    )
   

    if operation == "Histogram Stretching":
        result = histogram.histogram_stretching(image)
        st.image(result, channels="GRAY")

  
    elif operation == "Histogram Equalization":
        result = histogram.histogram_equalization(image)
        st.image(result, channels="GRAY")
    else:
         st.info("Select histogram operation")   
