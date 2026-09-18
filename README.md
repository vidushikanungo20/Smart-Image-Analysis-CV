 Smart Image Analysis System Using Computer Vision

 Introduction

Smart Image Analysis System is a modular Computer Vision program
written in Python using the OpenCV and NumPy libraries.

This program showcases several Computer Vision concepts
such as image preprocessing, image enhancement, histograms,
edge detection, contour detection, SIFT feature detection,
HOG feature extraction and image comparison.

 Objective

The key objectives of the project are:

1. Understanding basic image processing.
2. Practical usage of Computer Vision algorithms.
3. Extraction of useful features from images.
4. Comparing images using feature matching.
5. Developing a modular Computer Vision application.
6. Understanding practical implementation of OpenCV library.

 Functional Modules

1. Image Preprocessing

First of all, the image is turned into a grayscale one and Gaussian
filter is applied to it to remove any noise.

 2. Image Enhancement and Histogram

Histogram equalization algorithm is used to enhance image contrast.

 3. Edge Detection and Contours

Canny edge detector algorithm is used for edges detection.
Contours are detected based on edge map.

 4. SIFT Feature Detection

SIFT algorithm is used for detection of keypoints and
visual features in an image.

 5. HOG Feature Extraction

HOG (Histogram of Oriented Gradients) is applied to find
gradient-based features from an image.

 6. Image Matching

Brute Force matching and the ratio test are applied to
compare the SIFT descriptors of the two images.



- Python
- OpenCV
- NumPy
- Git
- GitHub



Install the dependencies:

```bash
pip install -r requirements.txt
