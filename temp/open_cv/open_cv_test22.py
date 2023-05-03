import cv2
import numpy as np
import sys
import random

sys.setrecursionlimit(100000)

src = cv2.imread("Image/son.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 467, 37)

# 빈 output 이미지 생성 (흰색)
output = np.full(binary.shape, 255, dtype=np.uint8)

# 이미지의 높이와 너비
height, width = binary.shape

# 점진적으로 이미지를 보여주는 단위 설정
step = 1

visited = np.zeros_like(binary, dtype=bool)


def dfs(i, j):
    if i < 0 or i >= height or j < 0 or j >= width or visited[i, j] or binary[i, j] != 0:
        return

    visited[i, j] = True
    output[max(0, i-4*step):min(i+5*step, height), max(0, j-4*step):min(j+5*step, width)
           ] = binary[max(0, i-4*step):min(i+5*step, height), max(0, j-4*step):min(j+5*step, width)]
    output[i, j] = random.randint(0, 150)

    ran_show = int(random.randrange(1, 1000))

    if ((i * j) % ran_show) == 0:
        cv2.imshow("output", output)
        cv2.waitKey(2)

    offsets = list(range(-4*step, 5*step, step))
    random.shuffle(offsets)

    for k in offsets:
        for l in offsets:
            ni, nj = i + k, j + l
            dfs(ni, nj)


# 시작점 찾기 (검은 픽셀 중 하나)
start_i, start_j = None, None
for i in range(0, height, step):
    for j in range(0, width, step):
        if binary[i, j] == 0 and not visited[i, j]:
            start_i, start_j = i, j
            dfs(start_i, start_j)
cv2.imshow("output", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
