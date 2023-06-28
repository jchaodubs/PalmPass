import cv2
import time
import os
import HandTrackingModule as htm

wCam,hCam = 640,480

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

folderPath = "FingerImage"
myList = os.listdir(folderPath)
#print(myList)
overlayList=[]
for imgPath in myList:
    image = cv2.imread(f'{folderPath}/{imgPath}')
    #print(f'{folderPath}/{imgPath}')
    overlayList.append(image)


assert(len(overlayList)==6)#number of images

detector = htm.handDetector(detectionCon = 0.75)

while True:

    success, img = cap.read()
    img = detector.findHands(img)
    
    #display hand image
    h,w,c = overlayList[1].shape
    img[0:h,0:w] = overlayList[1]

    cv2.imshow("Image",img)
    cv2.waitKey(1)