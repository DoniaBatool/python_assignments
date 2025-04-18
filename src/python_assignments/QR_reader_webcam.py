import cv2
from pyzbar.pyzbar import decode
import time

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

camera = True
while camera == True:
    success,frame = cam.read()
    for i in decode(frame):
        print(i.type)
        print(i.data.decode('utf-8'))
        time.sleep(6)

        cv2.imshow("OurQr_Code_Scanner",frame)

        cv2.waitKey(3)
