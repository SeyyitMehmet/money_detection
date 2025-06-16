import cv2 as cv
import numpy as np

events=[i for i in dir(cv) if'EVENT' in i]
print(events)

def ciz(event,x,y,flags,param):
    if flags & cv.EVENT_FLAG_LBUTTON:
       
        cv.circle(siyah_ekran,(x,y),100,(255,255,0),)

siyah_ekran=np.zeros((512,512,3),np.uint8)
cv.namedWindow("cerceve")
cv.setMouseCallback("cerceve",ciz)
while 1:
    cv.imshow("cerceve",siyah_ekran)
    k=cv.waitKey(20)
    if k ==ord("q"):
        break

cv.destroyAllWindows()
