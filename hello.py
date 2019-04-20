#!/usr/bin/python
# -*- coding: utf-8 -*-
#import numpy
import cv2
import showPhoto
import getGray

'''
img = cv2.imread('t.jpg')
img = getGray.getGray(img)
showPhoto.showPhoto(img)
'''

# 待检测的图片路径
imagepath = r'./t.jpg'

# 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')

# 读取图片
image = cv2.imread(imagepath)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# 探测图片中的人脸
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor = 1.15,
    minNeighbors = 5,
    minSize = (5,5),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "发现{0}个人脸!".format(len(faces))

for(x,y,w,h) in faces:
    # cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
    cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)

cv2.imshow("Find Faces!",image)
cv2.waitKey(0)