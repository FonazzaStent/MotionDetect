import cv2
import time
import time as t
import os
import shutil
import glob

if not os.path.exists("log.txt"):
    logfile=open("log.txt",'w')
    logfile.close()
logfile=open("log.txt",'a')
logfile.write(time.strftime("%d/%m/%Y %H:%M:%S"+"\n"))
logfile.close()

if not os.path.exists("capture"):
    os.makedirs("capture")

cap=cv2.VideoCapture(0)
ret1,frame1= cap.read()
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)
cv2.imshow('window',frame1)
imgnum= 0
"""for n in range (10,0,-1):
    t.sleep(1)
    print(n)"""
count=1
while(True):
    ret2,frame2=cap.read()
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)
    deltaframe=cv2.absdiff(gray1,gray2)

    threshold = cv2.threshold(deltaframe, 25, 255, cv2.THRESH_BINARY)[1]
    threshold = cv2.dilate(threshold,None)

    countour,heirarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in countour:

        if cv2.contourArea(i) <50:

            (x, y, w, h) = cv2.boundingRect(i)

            if imgnum<10000000:
                if count==1:
                    cv2.imwrite('./capture/capture'+str(imgnum)+'.jpg',frame2)
                    imgnum=imgnum+1
            ret1,frame1= cap.read()
            gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)
            ret2,frame2=cap.read()
            gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)
            deltaframe=cv2.absdiff(gray1,gray2)
            count=count+1
            if count>10:
                count=1
    cv2.imshow('window',frame2)
    if cv2.waitKey(20) == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()


