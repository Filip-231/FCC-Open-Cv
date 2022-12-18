import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../Resources/Photos/park.jpg")
cv.imshow("Boston", img)

# plt.imshow(img)
# plt.show()

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# BGR to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# bgr to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

# bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# hsv to bgr
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV_BGR", hsv_bgr)


cv.waitKey(0)
