import cv2
import numpy as np
import sys
import random

sys.setrecursionlimit(100000)

src = cv2.imread("Image/fable9.png")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 467, 37)


def initial_sand_color():
    r = random.randint(30, 70)
    g = random.randint(0, 50)
    b = random.randint(0, 50)
    return (b, g, r)


def random_sand_color():
    r = random.randint(160, 205)
    g = random.randint(120, 180)
    b = random.randint(40, 80)
    return (b, g, r)


output = np.zeros((*binary.shape, 3), dtype=np.uint8)

height, width = binary.shape

for i in range(height):
    for j in range(width):
        output[i, j] = initial_sand_color()

visited = np.zeros_like(binary, dtype=bool)


def dfs(i, j, step):
    if i < 0 or i >= height or j < 0 or j >= width or visited[i, j] or binary[i, j] != 0:
        return

    visited[i, j] = True
    output[i, j] = random_sand_color()

    ran_show = int(random.randrange(10000, 30000))

    if ((i * j) % (ran_show)) == 0:
        cv2.imshow("output", output)
        cv2.waitKey(50)

    # 다양한 방향으로 이동하기 위한 방향 벡터
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]
    random.shuffle(directions)

    for dx, dy in directions:
        ni, nj = i + dx * step, j + dy * step
        dfs(ni, nj, step)


start_i, start_j = None, None
for i in range(0, height):
    for j in range(0, width):
        if binary[i, j] == 0 and not visited[i, j]:
            start_i, start_j = i, j
            step = random.randint(1, 3)
            dfs(start_i, start_j, step)

# 부드러운 선을 위해 가우시안 블러 적용
output = cv2.GaussianBlur(output, (3, 3), 0)

cv2.waitKey(0)
cv2.destroyAllWindows()
