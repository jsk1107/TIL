import sys
import cv2
import numpy as np


src = cv2.imread('data/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image open failed')
    sys.exit()


kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
# 128을 더해서 픽셀값이 급격하게 감소하는 부분을 검정색으로 표현 되게끔 한다.
dst = cv2.filter2D(src, -1, kernel, delta=128)

dx = cv2.Sobel(src, -1, 1, 0, delta=128)
dy = cv2.Sobel(src, -1, 0, 1, delta=128)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()
cv2.destroyAllWindows()