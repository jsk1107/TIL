import cv2
import sys


src = cv2.imread('data/noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image open failed')
    sys.exit()

""" 잡음 제거이지만 약간 블러링 되는 효과도 있다. """
dst = cv2.medianBlur(src, 3)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()