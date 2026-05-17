import cv2
import numpy as np

def average_filter(image, ksize):
    return cv2.blur(image, (ksize, ksize))


def laplacian_filter(image):
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    return np.uint8(np.absolute(laplacian))

def median_filter(image, ksize):
    return cv2.medianBlur(image, ksize)

def max_filter(image, ksize):
    kernel = np.ones((ksize, ksize), np.uint8)
    return cv2.dilate(image, kernel)

def min_filter(image, ksize):
    kernel = np.ones((ksize, ksize), np.uint8)
    return cv2.erode(image, kernel)