import sys
import cv2
import numpy as np


src = cv2.imread('data/rose.bmp', cv2.IMREAD_COLOR)

if src is None:
    print('Image open failed')
    sys.exit()


src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

"""
    연산을 진행할때는 최대한 실수타입으로 변환해서 진행하는것이 더 정교하게 작업이 가능하다.
    물론 연산량은 좀 증가하겠지만...
"""
src_y = src_ycrcb[:, :, 0].astype(np.float32)
blr = cv2.GaussianBlur(src_y, (0, 0), 2.)
src_ycrcb[:, :, 0] = np.clip(2.*src_y - blr, 0, 255).astype(np.uint8)
dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()