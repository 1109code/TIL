import cv2
import numpy as np
import sys
import random

sys.setrecursionlimit(100000)

src = cv2.imread("Image/fable8.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 467, 37)

# 초기 페이지를 모래색으로 채우기


def initial_sand_color():
    # r = random.randint(210, 250)
    # g = random.randint(180, 220)
    # b = random.randint(130, 170)
    r = random.randint(30, 70)
    g = random.randint(0, 50)
    b = random.randint(0, 50)
    # r = random.randint(210, 255)
    # g = random.randint(170, 230)
    # b = random.randint(90, 130)
    return (b, g, r)

# 그림을 그릴 때 사용할 어두운 모래색 정의


def random_sand_color():
    r = random.randint(210, 255)
    g = random.randint(170, 230)
    b = random.randint(90, 130)
    # r = random.randint(30, 70)
    # g = random.randint(0, 50)
    # b = random.randint(0, 50)
    return (b, g, r)


output = np.zeros((*binary.shape, 3), dtype=np.uint8)

# 이미지의 높이와 너비
height, width = binary.shape

# 모든 픽셀을 모래색으로 채우기
for i in range(height):
    for j in range(width):
        output[i, j] = initial_sand_color()
        # output[i, j] = (0, 0, 255)


# step = random.randint(1, 3)
step = 1
visited = np.zeros_like(binary, dtype=bool)


def dfs(i, j):
    if i < 0 or i >= height or j < 0 or j >= width or visited[i, j] or binary[i, j] != 0:
        return

    visited[i, j] = True
    output[i, j] = random_sand_color()

    ran_show = int(random.randrange(1, 1000))

    if ((i * j) % ran_show * 30) == 0:
        cv2.imshow("output", output)
        cv2.waitKey(5)

    # step = random.randint(1, 3)

    offsets = list(range(-1*step, 3 * step, step))
    random.shuffle(offsets)

    for k in offsets:
        for l in offsets:
            ni, nj = i + k, j + l
            dfs(ni, nj)


# step = 1
start_i, start_j = None, None
for i in range(0, height, step):
    for j in range(0, width, step):
        if binary[i, j] == 0 and not visited[i, j]:
            start_i, start_j = i, j
            dfs(start_i, start_j)
cv2.imshow("output", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
