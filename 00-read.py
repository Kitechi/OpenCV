import cv2 as cv

img = cv.imread('C:/Users/g2019/OneDrive/Desktop/Programing/VS_Code/OpenCV/Photo/github-logo.png')

cv.imshow('github-logo',img)

capture = cv.VideoCapture(0)    #providing argument of 0 will capture with your laptop webcam
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

   # cv.waitKey(0)
