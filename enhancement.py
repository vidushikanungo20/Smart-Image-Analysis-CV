import cv2
import numpy as np

def enhance_image(img):

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    enhanced = cv2.equalizeHist(gray)

    return enhanced

def histogram_data(img):

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    hist = cv2.calcHist(
        [gray],
        [0],
        None,
        [256],
        [0, 256]
    )

    return hist.flatten()
