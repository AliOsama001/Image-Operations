import streamlit as st
import numpy as np
import cv2


def internal_boundary(image, k):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k, k))
    eroded = cv2.erode(image, kernel)
    return cv2.subtract(image, eroded)

def external_boundary(image, k):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k, k))
    dilated = cv2.dilate(image, kernel)
    return cv2.subtract(dilated, image)

def morphological_gradient(image, k):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k, k))
    return cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)