# -*- coding: utf-8 -*-
import cv2

imgPath = 't.jpg'
img = cv2.imread(imgPath)
frame_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow('testImg1', frame_gray)
frame_gray = cv2.equalizeHist(frame_gray) 
cv2.imshow('testImg2', frame_gray)
cv2.waitKey(0)

print('--(!)Error loading eyes cascade')
