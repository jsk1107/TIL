import cv2
import sys


src = cv2.imread('data/field.bmp')

if src is None:
    print('Image open failed')
    sys.exit()

""" 컬러영상의 평활화는 YCrCb 성분으로 바꾼 후 Y성분을 조절한다. """
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
planes = cv2.split(src_ycrcb)
planes[0] = cv2.equalizeHist(planes[0])
dst_ycrcb = cv2.merge(planes)
dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)

""" imshow는 bgr 색상을 받는다. """
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()