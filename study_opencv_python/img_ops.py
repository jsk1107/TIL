import numpy as np
import cv2


""" 영상 생성하기 """
# img1 = np.empty((240, 320), dtype=np.uint8) # 랜덤값으로 채워진 Gray Img
# img2 = np.zeros((240, 320, 3), dtype=np.uint8) # 0으로 채워진 Color Img
# img3 = np.ones((240, 320, 3), dtype=np.uint8) # 1로 채워진 Color Img
# img4 = np.full((240, 320, 3), (0, 0, 255), dtype=np.uint8) # (0, 0, 255)값 채워진 Color Img

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)
# cv2.imshow('img4', img4)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

""" 영상 복사하기 """
# img1 = cv2.imread('data/HappyFish.jpg')
# img2 = img1 # img1과 같은 주소를 참조
# img3 = img1.copy() # 참조 주소를 변경하여 복사함.
#
# img1[:, :] = (0, 255, 255)
#
# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

""" 영상 부분 복사하기 """
img1 = cv2.imread('data/HappyFish.jpg')
img2 = img1[40:120, 30:150]
img3 = img1[40:120, 30:150].copy()

img1[:, :] = (0, 255, 255)
# img1와 img2는 같은 주소를 참조하기 때문에,
# img2를 mask 영상처럼 사용하여 ROI를 셋팅하면 img1에도 적용이 된다
# (같은 주소를 참조하고 있기 때문에).

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()