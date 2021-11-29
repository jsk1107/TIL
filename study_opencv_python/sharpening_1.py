import sys
import cv2
import numpy as np


src = cv2.imread('data/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image open failed')
    sys.exit()

blr = cv2.GaussianBlur(src, (0, 0), 2)

""" 입력영상은 2배하고 blr 영상은 1배해서 뺀다(부호가 음수이기 때문에) """
# dst = cv2.addWeighted(src, 2, blr, -1)
dst = np.clip(2.*src - blr, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('blr', blr)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()