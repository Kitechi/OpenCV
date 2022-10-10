import cv2 as cv

img = cv.imread('C:/Users/g2019/OneDrive/Desktop/Programing/VS_Code/OpenCV/Photo/github-icon-clipart-7.png')

cv.imshow('github-logo',img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

img_resized = rescaleFrame(img,0.25)
cv.imshow('resized_logo', img_resized)

capture = cv.VideoCapture(0)    #providing argument of 0 will capture with your laptop webcam
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
