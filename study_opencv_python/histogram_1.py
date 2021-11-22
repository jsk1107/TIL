import cv2
import sys
import matplotlib.pyplot as plt

""" Gray 영상 히스토그램 """
src = cv2.imread('data/lenna.bmp', cv2.IMREAD_GRAYSCALE)


if src is None:
    print('Image open failed')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256])

cv2.imshow('src', src)

cv2.waitKey(1)

plt.plot(hist)
plt.show()


""" 컬러 영상 히스토그램 """
src = cv2.imread('data/lenna.bmp', cv2.IMREAD_COLOR)

if src is None:
    print('Image open failed')
    sys.exit()

color = ['b', 'g', 'r']
bgr_planes = cv2.split(src)

for (p, c) in zip(bgr_planes, color):

    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)

cv2.imshow('src', src)
cv2.waitKey(1)
plt.show()