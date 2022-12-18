import cv2 as cv
import numpy as np
import os


haar_cascade = cv.CascadeClassifier("haar_face.xml")

# features = np.load("features.npy")
#
# labels = np.load("labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]


img = cv.imread(r"../Resources/Faces/val/elton_john/1.jpg")


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces_rect:
    print(x, y, w, h)  # coordinates of detected face
    faces_roi = gray[y : y + h, x : x + h]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f"label = { label} with confidence of {confidence}")
    cv.putText(
        img,
        str(people[label]),
        (20, 20),
        cv.FONT_HERSHEY_COMPLEX,
        1.0,
        (0, 255, 0),
        thickness=2,
    )
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow("detect", img)

cv.waitKey(0)
