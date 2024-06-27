import os
import cv2

img=cv2.imread(os.path.join('.','Data1','image.png'))

resized=cv2.resize(img,(640,360))

print(img.shape)
print(resized.shape)

cv2.imshow('img1',resized)
cv2.imshow('img2',img)
cv2.waitKey(0)