import cv2
import numpy as np
img = cv2.imread('Halo.jpg',cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,imgbin01 = cv2.threshold (gray,128,255,cv2.THRESH_BINARY)
imgbin02 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('imagecolor',img)
cv2.imshow('imagegray',gray)
cv2.imshow('imagebin',imgbin01)
cv2.imshow('imageadapbin',imgbin02)
cv2.waitKey(0)