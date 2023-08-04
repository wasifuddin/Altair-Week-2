# pip install opencv-contrib-python
# pip install numpy


import cv2
import numpy as np


def detect_red_and_white_regions(img):
    # Converting BGR to HSV color space
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Defining the lower and upper threshold for red color
    lower_red = np.array([165, 134, 101])
    upper_red = np.array([179, 255, 255])

    # Creating mask to detect red region
    red_mask = cv2.inRange(hsv_img, lower_red, upper_red)
    # Showing Red Mask
    cv2.imshow("Red Mask", red_mask)
    # Applying Red Mask to Original Image
    red_detect_img = cv2.bitwise_and(img, img, mask=red_mask)
    # Showing Red Detected Original Image
    cv2.imshow("Red Detection", red_detect_img)

    # Defining the lower and upper threshold for white color
    lower_white = np.array([0, 0, 162])
    upper_white = np.array([179, 30, 255])
    # Creating mask to detect white region
    white_mask = cv2.inRange(hsv_img, lower_white, upper_white)
    # Showing the white mask
    cv2.imshow("White Mask", white_mask)
    # Applying White Mask to Original Image
    white_detect_img = cv2.bitwise_and(img, img, mask=white_mask)
    # Showing White Detected Original Image
    cv2.imshow("White Detection", white_detect_img)

    # Combining the Red and White Mask
    final_mask = red_mask + white_mask

    # Applying the mask to Actual Image to detect the Red and White regions
    traced_regions = cv2.bitwise_and(img, img, mask=final_mask)

    # Displaying the detected regions
    cv2.imshow('Original Detected Regions', traced_regions)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Return the final mask
    return final_mask


def analyze_goat(img_array):
    # Calculating the Min Max and Average Pixel Values
    min_val = np.min(img_array)
    max_val = np.max(img_array)
    avg_val = round(np.mean(img_array), 2)

    # Counting the Number of Zero and Non-Zero Pixel Number
    non_zero_pix_no = np.count_nonzero(img_array)
    zero_pix_no = img_array.size - non_zero_pix_no

    print("Minimum Pixel Value:", min_val)
    print("Maximum Pixel Value:", max_val)
    print("Average Pixel Value:", avg_val)
    print("Total Non Zero Pixels:", non_zero_pix_no)
    print("Total Zero Pixels:", zero_pix_no)


if __name__ == "__main__":
    # Image File Path
    img_path = 'GOAT.jpg'

    # Reading the Image
    img = cv2.imread(img_path)

    # Function to detect Red and White Regions
    detect_red_and_white_regions(img)

    # Converting the image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Function to analyse the goat
    analyze_goat(img_gray)
