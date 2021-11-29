import sys
import cv2


src = cv2.imread('data/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image open failed')
    sys.exit()


""" 
    ksize를 (0, 0)으로 지정하여 sigmaX 값에 의해 자동으로 결정되도록 한다.
    ksize를 강제로 지정하는경우는 가우시안의 양쪽 끝을 짤라버림으로써 가우시안의 의미를 상실하게 된다.
"""

dst = cv2.GaussianBlur(src, (0, 0), 2)
dst2 = cv2.blur(src, (7, 7))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()