import sys
import cv2


src = cv2.imread('data/candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image open failed')
    sys.exit()


print('src.shape', src.shape)
print('src.dtype', src.dtype)

planes = cv2.split(src)

cv2.imshow('src', src)
cv2.imshow('planes[0]', planes[0])
cv2.imshow('planes[1]', planes[1])
cv2.imshow('planes[2]', planes[2])
cv2.waitKey()
cv2.destroyAllWindows()