import numpy as np
import cv2
import sys


src = cv2.imread('data/namecard.jpg')

if src is None:
    print('Image open failed')
    sys.exit()


w, h = 720, 400
srcQuad = np.array([[325, 307], [760, 369], [718, 611], [231, 515]], dtype=np.float32)
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], dtype=np.float32)

"""
    이동하기 전 위치가 이동한 후 위치로 갔을 때, 변환행렬을 출력해준다.
"""
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (w, h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()