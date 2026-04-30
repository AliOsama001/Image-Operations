
import streamlit as st
import cv2
import numpy as np
from streamlit_option_menu import option_menu
from src.ui import point_ops, color_ops, edge_detection, histogram, neighborhood_processing, mathematical_morphology, restoration, segmentation

st.set_page_config(page_title="Digital Image Processing System", layout="wide")

with st.sidebar:
    st.title("DIP Control Center")
    selected = option_menu(
        menu_title="Select Operation",
        options=["Home", "Point Operations", "Color Operations", "Edge Detection", "Histogram", "Neighborhood Processing", "Mathematical Morphology", "Restoration", "Segmentation"],
        icons=['house', 'brightness-high', 'palette', 'border-style', 'bar-chart-line', 'grid-3x3', 'bounding-box', 'magic', 'scissors'],
        default_index=0
    )

if selected == "Home":
    st.title("Please upload an image to start")
    uploaded_file = st.file_uploader("Upload Image to Start", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        st.session_state['main_image'] = opencv_image
        st.success("Image uploaded!")
        st.image(opencv_image, channels="BGR", caption="Selected Image Preview", width=300)
    else:
        st.info("Please upload an image to enable the processing modules.")

else:
    if 'main_image' not in st.session_state:
        st.error("Please go back to 'Home' and upload an image first.")
    else:
        st.title(f"{selected}")
        image = st.session_state['main_image']
        
        col_input, col_output = st.columns(2)
        
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", use_container_width=True)
            
        with col_output:
            st.subheader("Processing Panel")
            if selected == "Point Operations":
                point_ops.run_module(image)
            elif selected == "Color Operations":
                color_ops.run_module(image)
            elif selected == "Edge Detection":
                edge_detection.run_module(image)
            elif selected == "Histogram":
                histogram.run_module(image)
            elif selected == "Neighborhood Processing":
                neighborhood_processing.run_module(image)
            elif selected == "Mathematical Morphology":
                mathematical_morphology.run_module(image)
            elif selected == "Restoration":
                restoration.run_module(image)
            elif selected == "Segmentation":
                segmentation.run_module(image)