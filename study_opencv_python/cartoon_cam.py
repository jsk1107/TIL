import sys
import cv2
import numpy as np


def cartoon_filter(img):

    h, w = img.shape[:2]
    """ 이미지를 작게 resize하고 아래의 연산을 진행하고 다시 scale Up해주면 극적인 카툰 효과가 더 가미된다. """
    img = cv2.resize(img, (w//2, h//2))

    blr = cv2.bilateralFilter(img, -1, 20, 7)
    edge = 255 - cv2.Canny(img, 50, 120)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2RGB)
    dst = cv2.bitwise_and(blr, edge)

    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)

    return dst


def pencil_sketch(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray, (0, 0), 3)

    dst = cv2.divide(gray, blr, scale=255)
    dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

    return dst


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('video open failed')
    sys.exit()


cam_mode = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if cam_mode == 1:
        frame = cartoon_filter(frame)
    elif cam_mode == 2:
        frame = pencil_sketch(frame)

    cv2.imshow('frame', frame)
    key = cv2.waitKey()

    if key == 27:
        break
    elif key == ord(' '):
        cam_mode += 1
        if cam_mode == 3:
            cam_mode == 0