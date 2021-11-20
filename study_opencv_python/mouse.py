import sys
import cv2
import numpy as np


oldx = oldy = -1
def on_mouse(event, x, y, flags, param):
    global img, oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print(f'EVENT_LBUTTONDOWN: {x}, {y}')
    elif event == cv2.EVENT_LBUTTONUP:
        print(f'EVENT_LBUTTONUP: {x}, {y}')
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON: # flags를 비교할때는 논리연산자를 사용해야한다.
            # print(f'EVENT_MOUSEMOVE: {x}, {y}')
            """ 
                마우스 오버를 빠르게하면 circle은 빈 공간이 생긴다. 
                그래서 이전 좌표와 현재좌표를 직선으로 이어주는 작업을 한다.
            """
            # cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 5, lineType=cv2.LINE_AA)
            cv2.imshow('img', img)
            oldx, oldy = x, y

img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('img')
""" callback은 namedWindow가 떠 있는 상태에서 호출되어야 한다. """
cv2.setMouseCallback('img', on_mouse)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()