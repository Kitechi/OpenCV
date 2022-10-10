from turtle import shape
import cv2 as cv
import numpy as np

#creating blank image
blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('blank',blank)

# 1. Paint the image in certain colour
blank[:] = 0,255,0
#cv.imshow('Green',blank)

# 2. Paint certain part of the image in certain colour
blank[200:300, 300:400] = 0,0,255
#cv.imshow('Green with red box',blank)

# 3. Draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (255,255,0),thickness=2)
#cv.imshow('Box+rectangle',blank)

cv.rectangle(blank, (0,0), (250,500), (255,255,0),thickness=cv.FILLED)
#cv.imshow('Box+rectangle',blank)

# 4. Draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255), thickness=3)
cv.imshow('circle',blank)

# 5. Draw a line
cv.line(blank,(0,0), (blank.shape[1]//2,blank.shape[0]//2),(255,255,255), thickness=3)
cv.imshow('line',blank)

# 6. Write text
cv.putText(blank,'Hello, I Salah',(0,350),cv.FONT_HERSHEY_TRIPLEX,1.0, (0,255,0),2)
cv.imshow('image with text Hello',blank)


cv.waitKey(0)