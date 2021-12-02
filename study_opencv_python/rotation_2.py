import cv2
import sys


src = cv2.imread('data/tekapo.bmp')

if src is None:
    print('Image open failed')
    sys.exit()

h, w = src.shape[:2]
cp = (w / 2, h / 2)
rot = cv2.getRotationMatrix2D(cp, 20, 1)

dst = cv2.warpAffine(src, rot, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()