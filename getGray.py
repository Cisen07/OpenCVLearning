# -*- coding: utf-8 -*-
import cv2

def getGray(img):
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return grayImg