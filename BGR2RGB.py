import os
import cv2

#By default the format of imread is BGR
img=cv2.imread(os.path.join('.','Data1','image.png'))


#Convertng it to RGB
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Convertin to gray scale
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Converting to HSV
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('img',img)
cv2.imshow('img_rgb',img_rgb)
cv2.imshow('img_gray',img_gray)
cv2.imshow('img_hsv',img_hsv)
cv2.waitKey(0)