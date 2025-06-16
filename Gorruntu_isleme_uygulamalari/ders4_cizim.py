import cv2 as cv
import numpy as np


img=np.zeros((512,512,3),np.uint8)
cv.line(img,(0,0),(511,511),(255,0,0),5,1)
cv.rectangle(img,(400,0),(450,50),(0,255,0),5,2)
cv.imshow("ads",img)

k=cv.waitKey(0)
if k ==ord("s"):
    cv.destroyAllWindows()
