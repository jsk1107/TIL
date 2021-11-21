import cv2
import sys
import matplotlib.pyplot as plt


src1 = cv2.imread('data/lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('data/square.bmp', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image open failed')
    sys.exit()

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0, dtype=cv2.CV_8U)
dst3 = cv2.subtract(src1, src2)
dst4 = cv2.absdiff(src1, src2)

plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('dst1')
plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('dst2')
plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('dst3')
plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('dst4')
plt.show()