import sys
import cv2


cap1 = cv2.VideoCapture('data/woman.mp4')

if not cap1.isOpened():
    print('video open failed')
    sys.exit()

cap2 = cv2.VideoCapture('data/raining.mp4')

if not cap2.isOpened():
    print('video open failed')
    sys.exit()


w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
print(f'w * h: {w} * {h}')
print(f'frame_cnt1: {frame_cnt1}')
print(f'frame_cnt2: {frame_cnt2}')

fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))
do_composit = False

while True:
    ret1, frame1 = cap1.read()

    if not ret1:
        break

    if do_composit:
        ret2, frame2 = cap2.read()

        if not ret2:
            break

        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (80, 255, 255))
        cv2.copyTo(frame2, mask, frame1)

    out.write(frame1)
    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    if key == ord(' '):
        do_composit = not do_composit
    elif key == 27:
        break

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()