import streamlit as st
from src.core import point_ops 

def run_module(image):

    operation = st.selectbox(
        "Point Operation",
        ["None", "Addition", "Subtraction", "Division", "Complement"]
    )
    st.info("Select operation")

    if operation == "Addition":
        value = st.slider("Value", 0, 100, 10)
        st.image(point_ops.addition(image, value), channels="BGR")

    elif operation == "Subtraction":
        value = st.slider("Value", 0, 100, 10)
        st.image(point_ops.subtraction(image, value), channels="BGR")

    elif operation == "Division":
        value = st.slider("Divisor", 1, 10, 2)
        st.image(point_ops.division(image, value), channels="BGR")

    elif operation == "Complement":
        st.image(point_ops.complement(image), channels="BGR")
