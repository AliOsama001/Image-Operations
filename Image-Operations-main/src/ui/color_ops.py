import streamlit as st 
import numpy as np 
from src.core import color_ops

def run_module(image):

    operation = st.selectbox(
        "Color Operations",["None","Change Red","Swap Channels","Remove Channel"])

    st.info("Select an operation")
    if operation == "Change Red":
        value = st.slider("Red Intensity", 0, 100, 20)
        result = color_ops.change_red(image, value)
        st.image(result, channels="BGR")


    elif operation == "Swap Channels":
        result = color_ops.swap_channels(image)
        st.image(result)

    elif operation == "Remove Channel":
        channel = st.selectbox("Select Channel", ["Red", "Green", "Blue"])
        result = color_ops.remove_channel(image, channel)
        st.image(result, channels="BGR")

   