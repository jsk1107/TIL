import sys
import cv2

src = cv2.imread('data/lenna.bmp', cv2.IMREAD_COLOR)

if src is None:
    print('Image open failed')
    sys.exit()


"""
    아래와 같은 산식을 통해 연산을 하면 255 초과되는 값을 포화 시키지 않는다.
    256 이상의 값은 다시 0으로 표현하기 때문에 이미지가 부분적으로 검정색이 보이게 된다.
    dst = src + 100 (x)
    dst = np.clip(src+100., 0, 255).astype(np.uint8) (o)
"""

# (b, g, r, alpha) 순서
dst = cv2.add(src, (100, 100, 100, 0)) # -> scalar 100을 입력하면 (100, 0, 0, 0)으로 변환되서 입력됨.


cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()