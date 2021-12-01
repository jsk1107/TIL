import sys
import cv2


src = cv2.imread('data/lenna.bmp', cv2.IMREAD_COLOR)

if src is None:
    print('Image open failed')
    sys.exit()

"""
    sigmaColor는 픽셀값의 차이를 뜻하며 해당 값보다 작은경우는 자신과 같은 픽셀이라고 간주를하고
    큰 경우 다른값의 픽셀이라 간주하여 블러링을 처리한다.
    
    sigmaColor는 10~20사이, sigmaSpace는 5 이하로 주는것이 일반적이다.
"""

dst = cv2.bilateralFilter(src, -1, 10, 5)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()