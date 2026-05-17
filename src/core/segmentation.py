import streamlit as st
import numpy as np
import cv2
from src.core.neighborhood_processing import (median_filter,average_filter,laplacian_filter,max_filter,min_filter)

def outlier_removal(image):
    return median_filter(image, 3)

def gaussian_smoothing(image, k):
    if k % 2 == 0: 
        k += 1
    return cv2.GaussianBlur(image, (k, k), 0)

def global_threshold(image, t):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh_img = cv2.threshold(image, t, 255, cv2.THRESH_BINARY)
    return thresh_img

def automatic_threshold(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh_img = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh_img

def adaptive_threshold(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    adaptive_img = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )
    return adaptive_img