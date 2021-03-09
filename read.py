import cv2 as cv

img=cv.imread('Resources/Photos/cat_large.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame,scale=0.75):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)
    dimensions=(height,width)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
# capture=cv.VideoCapture('Resources/Videos/dog.mp4')

# while True:
#     isTrue,frame=capture.read()
#     cv.imshow('Video',frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()



cv.waitKey(0)