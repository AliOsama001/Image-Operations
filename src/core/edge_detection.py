import streamlit as st
import numpy as np
import cv2

def sobel_edge(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    
    sobel_combined = cv2.magnitude(sobelx, sobely)
    return np.uint8(np.clip(sobel_combined, 0, 255))