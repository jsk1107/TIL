import cv2


""" 마스크 영상을 이용한 영상 합성 """
src = cv2.imread('data/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('data/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('data/field.bmp', cv2.IMREAD_COLOR)

# cv2.copyTo(src, mask, dst) # src와 dst는 shape이 같아야하고 mask는 grayScale이어야 한다.

dst[mask > 0] = src[mask > 0]
# mask의 값이 0보다 큰 값에 대해서 boolean 행렬을 만들고,
# True인 곳에 대해서만 값을 가지고 온다.

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.imshow('mask', mask)
# cv2.waitKey()
# cv2.destroyAllWindows()


""" 마스크 영상을 이용한 영상 합성(PNG파일) """
src = cv2.imread('data/opencv-logo-white.png', cv2.IMREAD_UNCHANGED) # PNG파일은 4채널이기 때문에 UNCHANGED를 사용해야함
dst = cv2.imread('data/field.bmp', cv2.IMREAD_COLOR)

mask = src[:, :, -1]
src = src[:, :, 0:3]

# cv2.copyTo(src, mask, dst) # 합성이 안됨. src와 dst의 크기가 다르기 때문임.

h, w = src.shape[:2]

crop = dst[10:h+10, 10:w+10] # 현재 같은 주소를 참조하고있음을 주의!
cv2.copyTo(src, mask, crop) # crop은 dst와 같은 주소를 참조하고 있기 때문에 dst가 변경되는것을 볼 수 있다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()