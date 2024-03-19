import cv2
import os
import time


camera = cv2.VideoCapture(0)

label = "i love you"
size = 100

newDir = "data\\"+label

if not os.path.exists(newDir):
    os.makedirs(newDir)

curr = 0

while(curr<size):
    _, frame = camera.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("Camera", frame)
    cv2.imwrite(newDir+"\\"+str(curr)+".jpg",frame)
    curr+=1
    time.sleep(0.1)

    if (cv2.waitKey(1) == ord("q")):
        break

camera.release()
cv2.destroyWindow()