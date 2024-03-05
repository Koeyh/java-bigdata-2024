# file : opencvTemplete.py
# desc : OpenCV 기본형

import cv2

image = cv2.imread('./day09/coby.jpg', cv2.IMREAD_UNCHANGED) # 원본

height, width, channel = image.shape

cv2.imshow('Coby the cat', image)

cv2.waitKey(0)
cv2.destroyAllWindows()