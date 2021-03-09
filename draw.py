import cv2 as cv
import numpy as np

# img=cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('Cat',img)

blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow('blank',blank)
# blank[200:300,400:500]=0,255,0
# cv.imshow('green',blank)
# blank[:]=0,0,255
# cv.imshow('green',blank)
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2) #thickness=cv.FILLED
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1) #thickness=cv.FILLED
cv.imshow('Rectangle',blank)
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=2)
cv.imshow('Circle',blank)
cv.waitKey(0)
