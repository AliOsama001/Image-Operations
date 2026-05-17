import cv2
import numpy as np

def histogram_stretching(image):
    return cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

def histogram_equalization(image):
    if len(image.shape) == 3:
        ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
        ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
        return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
    else:
        return cv2.equalizeHist(image)