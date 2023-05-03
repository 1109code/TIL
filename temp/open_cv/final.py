import cv2
import numpy as np
import sys
import random
from collections import deque

sys.setrecursionlimit(100000)

src = cv2.imread("Image/fable8.jpg")

# Gaussian blur 적용
blurred_src = cv2.GaussianBlur(src, (3, 3), 300)

blockSize = 207  # 조절 가능한 값
C = 37  # 조절 가능한 값

gray = cv2.cvtColor(blurred_src, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize, C)


def initial_sand_color():
    r = random.randint(133, 173)
    g = random.randint(82, 122)
    b = random.randint(31, 71)
    return (b, g, r)


def random_sand_color():
    r = random.randint(40, 80)
    g = random.randint(0, 80)
    b = random.randint(0, 80)
    return (b, g, r)


output = np.zeros((*binary.shape, 3), dtype=np.uint8)

height, width = binary.shape

for i in range(height):
    for j in range(width):
        output[i, j] = initial_sand_color()

visited = np.zeros_like(binary, dtype=bool)


def bfs(i, j, step):
    queue = deque([(i, j)])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]

    while queue:
        i, j = queue.popleft()

        if i < 0 or i >= height or j < 0 or j >= width or visited[i, j] or binary[i, j] != 0:
            continue

        visited[i, j] = True
        output[i, j] = random_sand_color()

        ran_show = int(random.randrange(1000, 5000))

        if ((i * j) % (ran_show)) == 0:
            cv2.imshow("output", output)
            cv2.waitKey(10)

        random.shuffle(directions)

        for dx, dy in directions:
            ni, nj = i + dx * step, j + dy * step
            if random.random() < 0.5:
                queue.append((ni, nj))
            else:
                dfs(ni, nj, step)


def dfs(i, j, step):
    if i < 0 or i >= height or j < 0 or j >= width or visited[i, j] or binary[i, j] != 0:
        return

    visited[i, j] = True
    output[i, j] = random_sand_color()

    ran_show = int(random.randrange(5000, 10000))

    if ((i * j) % (ran_show)) == 0:
        cv2.imshow("output", output)
        cv2.waitKey(10)

    offsets = list(range(-1*step, 2 * step, step))
    random.shuffle(offsets)

    for k in offsets:
        for l in offsets:
            ni, nj = i + k, j + l
            # cv2.waitKey(1)
            dfs(ni, nj, step)


start_i, start_j = None, None
for i in range(0, height):
    for j in range(0, width):
        if binary[i, j] == 0 and not visited[i, j]:
            start_i, start_j = i, j
            step = 1
            if random.random() < 0.5:
                bfs(start_i, start_j, step)
            else:
                dfs(start_i, start_j, step)

# 부드러운 선을 위해 가우시안 블러 적용
output = cv2.GaussianBlur(output, (3, 3), 0)

cv2.waitKey(0)
cv2.destroyAllWindows()
