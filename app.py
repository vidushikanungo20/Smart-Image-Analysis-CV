import cv2

from preprocessing import preprocess_image
from enhancement import enhance_image, histogram_data
from feature_detection import detect_edges_and_contours
from sift_module import run_sift
from hog_module import run_hog
from image_matching import match_images

def load_image(path):
    img = cv2.imread(path)

    if img is None:
        raise FileNotFoundError(
            f"Could not read image: {path}"
        )

    return img

def main():

    print("\size===================================")
    print(" SMART IMAGE ANALYSIS SYSTEM")
    print("===================================")

    print("\n1. Image Preprocessing")
    print("2. Enhancement and Histogram")
    print("3. Edge and Contour Analysis")
    print("4. SIFT Feature Detection")
    print("5. HOG Feature Extraction")
    print("6. Image Matching")

    choice = input("\nChoose module (1-6): ").strip()

    path = input("Enter image path: ").strip()

    try:
        img = load_image(path)
    except FileNotFoundError as error:
        print(error)
        return

    if choice == "1":

        output = preprocess_image(img)

        cv2.imwrite(
            "results/preprocessed.jpg",
            output
        )

        print("Preprocessed image saved.")

    elif choice == "2":

        output = enhance_image(img)
        hist = histogram_data(img)

        cv2.imwrite(
            "results/enhanced.jpg",
            output
        )

        print("Enhanced image saved.")
        print("Histogram calculated.")
        print("First 10 histogram values:", hist[:10])

    elif choice == "3":

        edges, contours = detect_edges_and_contours(img)

        cv2.imwrite(
            "results/edges.jpg",
            edges
        )

        cv2.imwrite(
            "results/contours.jpg",
            contours
        )

        print("Edge and contour results saved.")

    elif choice == "4":

        output, count = run_sift(img)

        cv2.imwrite(
            "results/sift.jpg",
            output
        )

        print("SIFT keypoints detected:", count)

    elif choice == "5":

        output, length = run_hog(img)

        cv2.imwrite(
            "results/hog_visualization.jpg",
            output
        )

        print("HOG feature vector length:", length)

    elif choice == "6":

        second_path = input(
            "Enter second image path: "
        ).strip()

        try:
            img2 = load_image(second_path)
        except FileNotFoundError as error:
            print(error)
            return

        output, good = match_images(
            img,
            img2
        )

        cv2.imwrite(
            "results/matching.jpg",
            output
        )

        print("Good feature matches:", good)

    else:

        print("Invalid choice.")

if __name__ == "__main__":
    main()
