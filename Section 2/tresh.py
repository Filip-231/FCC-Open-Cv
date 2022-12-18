import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../Resources/Photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Gray", thresh)

threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow("Gray", thresh_inv)


# adaptive thresholding
adaptive_threshold = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3
)
cv.imshow("Adaptive", adaptive_threshold)
cv.waitKey(0)
