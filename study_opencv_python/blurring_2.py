import sys
import cv2


src = cv2.imread('data/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image open failed')
    sys.exit()


cv2.imshow('src' , src)
for ksize in (3, 5, 7):
    dst = cv2.blur(src, (ksize, ksize))
    desc = f"Mean: {ksize}x{ksize}"
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_TRIPLEX, 1.0, 255, 1, cv2.LINE_AA)
    cv2.imshow('dst', dst)
    cv2.waitKey()
cv2.destroyAllWindows()