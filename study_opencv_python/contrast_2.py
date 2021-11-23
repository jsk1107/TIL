import numpy as np
import cv2
import sys

src = cv2.imread('data/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image open failed')
    sys.exit()

"""
    src의 min을 0으로, max를 255로 맵핑하여 전체 분포를 늘려주는 효과가 생김.
"""
dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

""" 위처럼 normalize함수를 사용할 수도 있고, 직접 산식을 통해 구할 수 있다. """
gmin = np.min(src)
gmax = np.max(src)
transform = 255. * (src - gmin) / (gmax - gmin)
np.clip(transform, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
