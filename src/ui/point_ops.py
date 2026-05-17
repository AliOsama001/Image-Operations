import streamlit as st
from src.core import point_ops
from src.utils import show_images

def run_module(image):
    operation = st.selectbox(
        "Point Operation",
        ["None", "Addition", "Subtraction", "Division", "Complement"]
    )

    if operation == "Addition":
        value = st.slider("Value", 0, 100, 10)
        result = point_ops.addition(image, value)
        show_images(image, result, "BGR")

    elif operation == "Subtraction":
        value = st.slider("Value", 0, 100, 10)
        result = point_ops.subtraction(image, value)
        show_images(image, result, "BGR")

    elif operation == "Division":
        value = st.slider("Divisor", 1, 10, 2)
        result = point_ops.division(image, value)
        show_images(image, result, "BGR")

    elif operation == "Complement":
        result = point_ops.complement(image)
        show_images(image, result, "BGR")

    else:
        st.info("Select operation")
