import os
import cv2

#read video
path=os.path.join('.','Data1','file_example_MP4_480_1_5MG.mp4')

video=cv2.VideoCapture(path)

print(type(video))
#visualize video

ret=True

while ret:
    ret,frame=video.read()


    if ret:
        cv2.imshow('frame',frame)
        cv2.waitKey(2)

video.release()
cv2.destroyAllWindows()