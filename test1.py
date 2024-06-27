import cv2
import os
#read image
image_path=os.path.join('.','Data1','image.png')
image=cv2.imread(image_path)
#write image
cv2.imwrite(os.path.join('.','Data1','image_out1.png'),image)
#visualize image

cv2.imshow('image',image)
cv2.waitKey(5000)


cv2.destroyAllWindows()