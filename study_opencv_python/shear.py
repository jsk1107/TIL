import cv2
import sys
import numpy as np


src = cv2.imread('data/tekapo.bmp')

if src is None:
    print('Image open failed')
    sys.exit()

"""
    가로방향, 세로방향 이동은 0.
    y축의 이미지를 x축 방향으로 밀어냄.
    밀어내는 크기는 이미지의 height의 0.5크기 만큼 이동시킴.
"""
aff = np.array([[1, 0.5, 0], [0, 1, 0]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))
# h, w = src.shape[:2]
# dst = cv2.warpAffine(src, aff, (w+int(h*0.5), h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()