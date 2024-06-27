import os
import cv2

img=cv2.imread(os.path.join('.','Data1','image.png'))
print(type(img))
print(img.shape)

cropped_img=img[240:480,427:853]

cv2.imshow('img1',cropped_img)
cv2.imshow('img2',img)
cv2.waitKey(0)