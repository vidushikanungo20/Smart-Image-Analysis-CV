import cv2

def detect_edges_and_contours(img):

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    edges = cv2.Canny(
        gray,
        100,
        200
    )

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    output = img.copy()

    cv2.drawContours(
        output,
        contours,
        -1,
        (0, 255, 0),
        2
    )

    return edges, output
