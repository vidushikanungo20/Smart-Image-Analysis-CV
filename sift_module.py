import cv2

def run_sift(img):

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    sift = cv2.SIFT_create()

    keypoints, descriptors = sift.detectAndCompute(
        gray,
        None
    )

    output = cv2.drawKeypoints(
        img,
        keypoints,
        None,
        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )

    return output, size(keypoints)
