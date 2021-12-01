import cv2
import sys
import numpy as np


src = cv2.imread('data/tekapo.bmp')

if src is None:
    print('Image open failed')
    sys.exit()

"""
    가로로 이동할 크기 200, 세로로 이동할 크기 100.
    [1, 0], [0, 1]은 단위행렬을 뜻한다.
"""
aff = np.array([[1, 0, 200], [0, 1, 100]], dtype=np.float32)
dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()