import cv2
import numpy as np

def get_object_size(frame, object_contour):
    x, y, w, h = cv2.boundingRect(object_contour)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Calculate the size of the object in pixels
    object_size_pixels = w * h
    # Print or return the object size
    print("Object size (pixels):", object_size_pixels)
    # print("Object size (real-world units):", object_size_pixels / pixels_per_unit)
    return frame

def main():
    # Open the camera
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate through contours and find the contour with the largest area
        if contours:
            object_contour = max(contours, key=cv2.contourArea)
            frame = get_object_size(frame, object_contour)

        # Display the frame
        cv2.imshow('Object Size Measurement', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
