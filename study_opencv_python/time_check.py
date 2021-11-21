import sys
import cv2


img = cv2.imread('data/hongkong.jpg', cv2.IMREAD_COLOR)

if img is None:
    print('Image load failed')
    sys.exit()


tm = cv2.TickMeter()

tm.start()
edge = cv2.Canny(img, 50, 150)
tm.stop()
ms = tm.getTimeMilli()

print(f'Elapsed time: {ms}ms')