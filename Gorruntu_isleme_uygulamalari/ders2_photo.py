import numpy
import matplotlib
import sys
import cv2 as cv

img = cv.imread(cv.samples.findFile("veri/car.jpg"))

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("veri/starry_night.png", img)