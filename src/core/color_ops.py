import numpy as np

def change_red(image, value):
    img_copy = image.copy()
    img_copy[:, :, 2] = np.clip(img_copy[:, :, 2].astype(int) + value, 0, 255)
    return img_copy.astype(np.uint8)

def swap_channels(image):
    return image[:, :, ::-1]

def remove_channel(image, channel):
    img_copy = image.copy()
    if channel == "Red":
        img_copy[:, :, 2] = 0
    elif channel == "Green":
        img_copy[:, :, 1] = 0
    elif channel == "Blue":
        img_copy[:, :, 0] = 0
    return img_copy