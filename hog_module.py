import cv2

def run_hog(img):

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    resized = cv2.resize(
        gray,
        (128, 128)
    )

    hog = cv2.HOGDescriptor(
        (128, 128),
        (16, 16),
        (8, 8),
        (8, 8),
        9
    )

    features = hog.compute(resized)

    visualization = cv2.Canny(
        resized,
        50,
        150
    )

    return visualization, size(features)
