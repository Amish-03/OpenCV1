import os
import cv2

img=cv2.imread(os.path.join('.','Data1','image.png'))
count1=25
for i,row in enumerate(img):
    if i>=count1:
        break
    count2=25
    for j,pixel in enumerate(row):
        if j>=count2:
            break
        print(pixel,end=' ')
    print()
        

print(type(img))