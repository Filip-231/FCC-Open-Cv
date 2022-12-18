import cv2 as cv

img = cv.imread("../Resources/Photos/cats.jpg")
cv.imshow("Cats", img)

# Averaging
average = cv.blur(img, (7, 7))
cv.imshow("Average Blur", average)

# Gaussian
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("Gaus", gauss)

# Median
median = cv.medianBlur(img, 7)
cv.imshow("Median", median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)
