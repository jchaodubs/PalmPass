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

detector = htm.handDetector(detectionCon = 1)

tipIds=[4,8,12,16,20]#thumb,index,middle,ring,pinky

while True:

    success, img = cap.read()
    img = detector.findHands(img)
    numList = detector.findPosition(img,draw=False)
    #print(numList)
    if len(numList)!=0:
        fingers=[]

        #thumb
        if numList[tipIds[0]][1]<numList[tipIds[0]-1][1]:#index finger up, more minus = more dramatic, less = small
                fingers.append(1)
        else:
                fingers.append(0)
        
        #rest of hand
        for id in range(1,5):
            if numList[tipIds[id]][2]<numList[tipIds[id]-2][2]:#index finger up, more minus = more dramatic, less = small
                fingers.append(1)
            else:
                fingers.append(0)
        #print(fingers)
        totalFingers=fingers.count(1)
        print(totalFingers)
            
    
    #   display hand image
        h,w,c = overlayList[totalFingers-1].shape
        img[0:h,0:w] = overlayList[totalFingers-1]

        

    cv2.imshow("Image",img)
    cv2.waitKey(1)