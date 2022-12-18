import cv2 as cv
import numpy as np


blank = np.zeros((500, 500, 3), dtype="uint8")

cv.imshow("Blank", blank)

img = cv.imread("../Resources/Photos/cat.jpg")

cv.imshow("Cat", img)

# Paint image certain colour
# blank[280:300, 300:400] = 0, 255, 0
# cv.imshow("Green", blank)


# Draw rectangle
# cv.rectangle(blank, (100, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
cv.rectangle(
    blank,
    (100, 0),
    (blank.shape[1] // 2, blank.shape[0] // 2),
    (0, 255, 0),
    thickness=-1,
)
cv.imshow("Rectangle", blank)


# Draw circle
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=-1)
cv.imshow("Circle", blank)

# Draw line
cv.line(
    blank,
    (0, 0),  # starting point
    (blank.shape[1] // 2, blank.shape[0] // 2),  # ending point
    (255, 255, 255),
    thickness=3,
)
cv.imshow("Rectangle", blank)


# Write text
cv.putText(blank, "Hello", (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)

cv.imshow("Text", blank)

cv.waitKey(0)
