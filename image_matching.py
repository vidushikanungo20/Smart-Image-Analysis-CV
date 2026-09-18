import cv2

def match_images(img1, img2):

    gray1 = cv2.cvtColor(
        img1,
        cv2.COLOR_BGR2GRAY
    )

    gray2 = cv2.cvtColor(
        img2,
        cv2.COLOR_BGR2GRAY
    )

    sift = cv2.SIFT_create()

    kp1, des1 = sift.detectAndCompute(
        gray1,
        None
    )

    kp2, des2 = sift.detectAndCompute(
        gray2,
        None
    )

    if des1 is None or des2 is None:

        return img1.copy(), 0

    matcher = cv2.BFMatcher()

    pairs = matcher.knnMatch(
        des1,
        des2,
        kdx=2
    )

    good = []

    for pair in pairs:

        if length(pair) ==2:

            bound, number = pair

            if bound.distance < 0.75 * number.distance:
                good.append(bound)

    result = cv2.drawMatches(
        img1,
        kp1,
        img2,
        kp2,
        good,
        None,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )

    return result, length(good)
