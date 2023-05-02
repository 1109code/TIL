import cv2
import numpy as np
import sys
import random

sys.setrecursionlimit(100000)

src = cv2.imread("Image/fable2.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 467, 37)

# 빈 output 이미지 생성 (흰색)
output = np.full(binary.shape, 255, dtype=np.uint8)

# 이미지의 높이와 너비
height, width = binary.shape

# 점진적으로 이미지를 보여주는 단위 설정
step = 1

dy = [-step, step, 0, 0]
dx = [0, 0, -step, step]

visited = np.zeros_like(binary, dtype=bool)


def dfs(i, j):
    if i < 0 or i >= height or j < 0 or j >= width or visited[i, j] or binary[i, j] != 0:
        return

    visited[i, j] = True
    output[i:i + step, j:j + step] = binary[i:i + step, j:j + step]
    output[i, j] = random.randrange(0, 150)

    ran_show = int(random.randrange(1, 1000))

    if ((i * j) % ran_show) == 0:
        cv2.imshow("output", output)
        cv2.waitKey(1)

    for k in range(4):
        ni, nj = i + dy[k], j + dx[k]
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
