import cv2 as cv

# #Reading Photos
# img = cv.imread("../Resources/Photos/cat.jpg")
#
# cv.imshow("Cat", img)
#
# cv.waitKey(0)

# #Reading Videos
capture = cv.VideoCapture("../Resources/Videos/dog.mp4")
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord("d"):  # press "d" to close
        break

capture.release()
cv.destroyWindows()
