import cv2 as cv
import numpy as np

img = cv.imread("../Resources/Photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank", blank)

# mask = cv.rectangle(  # or circle
#     blank,
#     (img.shape[1] // 2, img.shape[0] // 2),
#     (img.shape[1] // 2 + 100, img.shape[0] // 2 + 100),
#     255,
#     -1,
# )

circle = cv.circle(  # or circle
    blank.copy(),
    (img.shape[1] // 2, img.shape[0] // 2),
    100,
    255,
    -1,
)

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)

cv.imshow("mask", weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow("mask", masked)


cv.waitKey(0)
