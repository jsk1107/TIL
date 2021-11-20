import cv2
import sys


img = cv2.imread('data/cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)

while True:
    """ key를 변수로 받은 후, 분기문을 설정해주어야한다. """
    key = cv2.waitKey()
    if key == 27:
        break
    elif key == ord('i'): # ord는 'i'의 아스키코드값을 반환해줌.
        img = ~img
        cv2.imshow('image', img)

cv2.destroyAllWindows()