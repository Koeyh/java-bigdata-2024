# file : p63_opencv.py
# desc : OpenCV 영상처리

import cv2


samplePath = './day09/earth.mp4'
cap = cv2.VideoCapture(samplePath) # 0은 웹캠 또는 문자열로 동영상 경로

while True:
    ret, frame = cap.read()

    if not ret:
        cap = cv2.VideoCapture(samplePath)
        continue

## 영상 편집
    blur = cv2.blur(frame, (10, 10))
    flip = cv2.flip(frame, 0) # 상하반전


    cv2.imshow('Original', frame)
    cv2.imshow('Blur', blur)
    cv2.imshow('Flip', flip)

    key = cv2.waitKey(5) # 5ms 딜레이
    if key == ord('q'): # 키보드 q로 중단 
        break
    elif key == ord('c'):
        cv2.imwrite('./day09/capt.jpg', frame) # c 입력 시 capt.jpg라는 이름으로 이미지 저장 

cap.release()
cv2.destroyAllWindows()