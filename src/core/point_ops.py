import numpy as np
import cv2

def addition(image, value):
    return cv2.add(image, np.uint8([value]))

def subtraction(image, value):
    return cv2.subtract(image, np.uint8([value]))

def division(image, value):
    if value == 0:
        return image
    return cv2.divide(image, np.uint8([value]))

def complement(image):
    return cv2.bitwise_not(image)