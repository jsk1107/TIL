import sys
import cv2


""" 카메라 열기 """
cap = cv2.VideoCapture(0) # int타입의 숫자는 카메라 장치를 의미함. 0은 기본 카메라 장치
cap = cv2.VideoCapture('data/video1.mp4')
if not cap.isOpened():
    print('camera open failed!')
    sys.exit()

""" 카메라 정보 얻기 """
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

""" 카메라 정보 설정하기 """
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

""" 영상에서 1 frame씩 받아오기 """
while True:
    ret, frame = cap.read()

    """ 영상의 맨 마지막 프레임이 들어온 이후 ret은 false가 되어서 while문 탈출 """
    if not ret:
        break

    """ 정지영상 처리 """
    edge = cv2.Canny(frame, 50, 150)

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)

    if cv2.waitKey(20) == 27: # ESC
        break

cap.release()
cv2.destroyAllWindows()