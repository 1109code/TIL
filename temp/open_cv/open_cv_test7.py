import cv2
import numpy as np
from collections import deque

src = cv2.imread("Image/son.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 467, 37)

# 빈 output 이미지 생성 (흰색)
output = np.full(binary.shape, 255, dtype=np.uint8)

# 이미지의 높이와 너비
height, width = binary.shape

# 점진적으로 이미지를 보여주는 단위 설정
step = 10

# 검은 픽셀 목록 생성
black_pixels = []
for i in range(0, height, step):
    for j in range(0, width, step):
        if binary[i, j] == 0:
            black_pixels.append((i, j))

# 검은 픽셀을 방문하면서 이미지 그리기
for i, j in black_pixels:
    output[i:i + step, j:j + step] = binary[i:i + step, j:j + step]
    cv2.imshow("output", output)
    cv2.waitKey(1)

cv2.waitKey(0)
cv2.destroyAllWindows()
