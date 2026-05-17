import streamlit as st
from src.core import point_ops

def run_module(image):
    operation = st.selectbox(
        "Point Operation",
        ["None", "Addition", "Subtraction", "Division", "Complement"]
    )

    if operation == "Addition":
        value = st.slider("Value", 0, 100, 10)
        result = point_ops.addition(image, value)
        
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    elif operation == "Subtraction":
        value = st.slider("Value", 0, 100, 10)
        result = point_ops.subtraction(image, value)
        
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    elif operation == "Division":
        value = st.slider("Divisor", 1, 10, 2)
        result = point_ops.division(image, value)
        
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")

    elif operation == "Complement":
        result = point_ops.complement(image)
        
        col_input, col_output = st.columns(2)
        with col_input:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width="stretch")
        with col_output:
            st.subheader("Output Image")
            st.image(result, channels="BGR")
    else:
        st.info("Select operation")
