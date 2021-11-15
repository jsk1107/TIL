import cv2
import os
import sys
sys.path.append('.')


""" 영상 불러오기 """
img1 = cv2.imread('data/cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('data/cat.bmp', cv2.IMREAD_COLOR)


""" 영상 불러오지 못하면 None이 들어온다. 확인하여 종료 """
if img1 is None or img2 is None:
    print('Image load failed')
    sys.exit()

h, w = img1.shape
print(img1.shape) # 640 x 480  (h, w)
print(img2.shape) # 640 x 480 x 3  (h, w, c)


""" 영상의 픽셀값 참조하기 """
x = 20
y = 10
p = img1[y, x]
print(p) # 238

p = img2[y, x]
print(p) # [237, 242, 232]


""" 영상의 특정 위치 픽셀값 변경하기 """
# 이중포문을 통한 변경. 절대 사용하지 말것. 연산속도 최악
for y in range(h):
    for x in range(w):
        img1[y, x] = 0
        img2[y, x] = (0, 255, 255)

# 아래와 같이 영상 좌표를 Slicing하여 진행.
img1[:, :] = 0
img2[:, :] = (0, 255, 255)