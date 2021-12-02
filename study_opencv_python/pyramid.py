import sys
import cv2


src = cv2.imread('data/cat.bmp')

if src is None:
    print('Image open failed')
    sys.exit()


rc = (250, 120, 200, 200) # (x, y, w, h)

cpy = src.copy()
cv2.rectangle(cpy, rc, (0, 0, 255), 2)
cv2.imshow('src', cpy)
cv2.waitKey()


for i in range(1, 4):
    src = cv2.pyrDown(src)
    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift=i)
    cv2.imshow('src', cpy)
    cv2.waitKey()
cv2.destroyAllWindows()