import streamlit as st
from src.core import color_ops
from src.utils import show_images

def run_module(image):
    operation = st.selectbox(
        "Color Operations", 
        ["None", "Change Red", "Swap Channels", "Remove Channel"]
    )

    if operation == "Change Red":
        value = st.slider("Red Intensity", -255, 255, 0)
        result = color_ops.change_red(image, value)
        
        show_images(image, result, "BGR")

    elif operation == "Swap Channels":
        result = color_ops.swap_channels(image)
        show_images(image, result, "BGR")

    elif operation == "Remove Channel":
        channel = st.selectbox("Select Channel", ["Red", "Green", "Blue"])
        result = color_ops.remove_channel(image, channel)
        show_images(image, result, "BGR")

    else:
        st.info("Select Color operation")