import streamlit as st 
import numpy as np 
from src.core import color_ops

import streamlit as st
import numpy as np
import cv2
from src.core import color_ops

def run_module(image):
    operation = st.selectbox(
        "Color Operations", 
        ["None", "Change Red", "Swap Channels", "Remove Channel"]
    )

    if operation == "Change Red":
        value = st.slider("Red Intensity", -255, 255, 0)
        result = color_ops.change_red(image, value)
        st.image(result, channels="BGR")

    elif operation == "Swap Channels":
        result = color_ops.swap_channels(image)
        st.image(result, channels="BGR")

    elif operation == "Remove Channel":
        channel = st.selectbox("Select Channel", ["Red", "Green", "Blue"])
        result = color_ops.remove_channel(image, channel)
        st.image(result, channels="BGR")
        
    else:
        st.info("Select Color operation")