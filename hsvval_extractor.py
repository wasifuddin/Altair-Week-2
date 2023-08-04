# pip install cvzone
import cv2
from cvzone.ColorModule import ColorFinder
# Creating Color Finding Object
myColorFinder = ColorFinder(True)

while True:
    # Reading the Image
    img = cv2.imread('GOAT.jpg')
    # Processing the img according to values in the trackbar
    img, mask = myColorFinder.update(img)
    # Showing the image
    cv2.imshow("Color Detection", img)
    # Setting cv2.waitkey to 1 to continuously see the updated image
    cv2.waitKey(1)
