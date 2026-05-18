import numpy as np
import cv2


def average_filter(image, ksize):
    return cv2.blur(image, (ksize, ksize))

def median_filter(image, ksize):
    return cv2.medianBlur(image, ksize)

def outlier_method(image, threshold=30):
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()
        
    blur_img = cv2.blur(gray, (3, 3))
    diff = cv2.absdiff(gray, blur_img)
    result = np.where(diff > threshold, blur_img, gray)
    return result

def image_averaging(image_list):
    return np.mean(image_list, axis=0).astype(np.uint8)

def laplacian_filter(image):
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    return np.uint8(np.absolute(laplacian))