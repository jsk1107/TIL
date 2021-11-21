import sys
import cv2
import numpy as np


""" 영상 불러오기 """
cap1 = cv2.VideoCapture('data/video1.mp4')
cap2 = cv2.VideoCapture('data/video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed')
    sys.exit()

""" 두 영상의 크기와 FPS는 같다고 가정 """
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2)

print(f'frame_cnt1: {frame_cnt1}')
print(f'frame_cnt2: {frame_cnt2}')
print(f'fps: {fps}')

delay = int(1000/fps) # 프레임간 시간간격

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

""" 출력 동영상 객체를 생성한다 """
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

""" 맨 마지막 48프레임을 제외한 나머지 프레임을 가져온다 """
for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()

    if not ret1:
        break

    out.write(frame1)
    cv2.imshow('frame', frame1)
    cv2.waitKey(delay)

""" 합성하는 구간 """
for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    dx = int(w * i / effect_frames)

    """ 프레임 밀어내기 """
    # frame = np.zeros((h, w, 3), dtype=np.uint8)
    # frame[:, 0:dx] = frame2[:, 0:dx]
    # frame[:, dx:w] = frame1[:, dx:w]

    """ 디졸브 """
    alpha = 1.0 - i / effect_frames
    frame = cv2.addWeighted(frame1, alpha, frame2, 1-alpha, 0)

    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.waitKey(delay)

""" 맨 앞 48프레임을 제외한 나머지 프레임을 가져온다. """
for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()

    if not ret2:
        break

    out.write(frame2)
    cv2.imshow('frame', frame2)
    cv2.waitKey(delay)

cap1.release()
cap2.release()
out.release()