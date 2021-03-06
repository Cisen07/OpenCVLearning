from __future__ import print_function
import cv2 as cv
import argparse
def detectAndDisplay(frame):
    # 转变为灰度图
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  
    # 直方图均衡化，通过拉伸像素强度分布范围来增强图像对比度，从而提高图片质量
    frame_gray = cv.equalizeHist(frame_gray)    
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
    cv.imshow('Capture - Face detection', frame)
# 创建ArgumentParser()对象
parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
# 调用add_argument()方法添加参数
parser.add_argument('--face_cascade', help='Path to face cascade.', default='./haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='./haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera devide number.', type=int, default=0)
# 使用parse_args()解析添加的参数
args = parser.parse_args()

face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
# 1. Load the cascades    加载级联分类器
if not face_cascade.load(face_cascade_name):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(eyes_cascade_name):
    print('--(!)Error loading eyes cascade')
    exit(0)
# 从设备的摄像头获取图像
camera_device = args.camera
# 2. Read the video stream
cap = cv.VideoCapture(camera_device)
# cap = cv.VideoCapture(0)  # 用这一句替代上两句也可以
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame)
    if cv.waitKey(10) == 27:    # 键入esc则退出，27是esc的ASCII码
        break