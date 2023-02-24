import cv2
import numpy as np
# img = cv2.imread('lily.png')

# img_resize = cv2.resize(img, (0,0), fx=0.20, fy=0.20)

# cv2.imshow("image", img_resize);
# cv2.waitKey(0)

vdo = cv2.VideoCapture(1)
vdo.set(3,640)
vdo.set(4,480)
while True:
    success,frame = vdo.read()
    img = cv2.flip(frame, 1)
    colorImg= cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow("RGB Image", colorImg)
    
    if cv2.waitKey(1) & 0xFF == ord('c'):
      break
