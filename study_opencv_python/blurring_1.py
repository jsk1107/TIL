import sys
import numpy as np
import cv2


src = cv2.imread('data/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image open failed')
    sys.exit()


kernel = np.ones((3, 3), dtype=np.float) / 9.
dst = cv2.filter2D(src, -1, kernel)
dst2 = cv2.blur(src, (3, 3))


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()

