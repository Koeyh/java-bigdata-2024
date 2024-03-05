# file : p64_opencv.py
# desc : OpenCV 영상처리

import cv2


samplePath = './day09/news.mp4'
faceCascade = cv2.CascadeClassifier('./day09/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(samplePath) # 0은 웹캠 또는 문자열로 동영상 경로

while True:
    ret, frame = cap.read()

    if not ret:
        cap = cv2.VideoCapture(samplePath)
        continue

## 영상에서 사람 얼굴 검출
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20,20)
        )
   
    
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), color=(0,255,0), thickness=2) # BGR 순서로 색상 입력


    cv2.imshow('Original', frame)
    cv2.imshow('gray', gray) # gray에는 얼굴인식 설정 X


    key = cv2.waitKey(5) # 5ms 딜레이
    if key == ord('q'): # 키보드 q로 중단 
        break

cap.release()
cv2.destroyAllWindows()