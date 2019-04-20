# -*- coding: utf-8 -*-
import cv2

def showPhoto(img):
    #cv2.namedWindow('Image')
    #cv2.imshow('Image', img)
    res = cv2.resize(img, (400, 296), interpolation=cv2.INTER_CUBIC)   #interpolation是不同的插值方法
    cv2.imshow('Scale_Smile', res)
    cv2.waitKey(0)  #图片不会自动关闭