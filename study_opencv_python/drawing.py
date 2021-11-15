import numpy as np
import cv2


img = np.full((400, 400, 3), 255, np.uint8)

""" 직선 그리기 """
cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

""" 사각형 그리기 """
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2) # x,y,w,h 순서임
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1) # (x1, y1) (x2, y2)를 의미함. -1은 내부를 채워라는 의미

""" 원 그리기 """
# LINE_AA는 안티엘리어싱. 부드럽게 표현할때 사용. 원이나 문자열을 표현할때 많이 사용한다.
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA) # LINE_AA는 안티엘리어싱. 부드럽게 표현할때 사용. 원이나 문자열을 표현할때 많이 사용한다.
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

""" 다각형 그리기 """
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
cv2.polylines(img, [pts], True, (255, 0, 255), 2) # 다각형 좌표를 받을때 꼭 List에 감싸서 주어야한다.

""" 문자열 출력 """
text = "Hello Opencv" + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)


cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()