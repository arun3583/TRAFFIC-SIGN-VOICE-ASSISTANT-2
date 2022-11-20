import cv2
import os
import matplotlib.pyplot as plt
cap=cv2.VideoCapture("/home/arun/PycharmProjects/GIT/MVI_1049.avi")
ret,frame=cap.read()
cv2.imshow('image show',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("hiii")