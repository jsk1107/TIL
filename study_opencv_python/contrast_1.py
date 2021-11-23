import numpy as np
import cv2
import sys

src = cv2.imread('data/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image open failed')
    sys.exit()

""" 명암비 조절 산식 """
alpha = 1.0
transform = (1 + alpha) * src - 128 * alpha

dst = np.clip(transform, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()