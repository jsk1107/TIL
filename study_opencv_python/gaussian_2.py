import sys
import cv2


src = cv2.imread('data/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image open failed')
    sys.exit()


cv2.imshow('src' , src)
for sigma in range(1, 6):
    dst = cv2.GaussianBlur(src, (0, 0), sigma)
    desc = f"Sigma: {sigma}"
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_TRIPLEX, 1.0, 255, 1, cv2.LINE_AA)
    cv2.imshow('dst', dst)
    cv2.waitKey()
cv2.destroyAllWindows()