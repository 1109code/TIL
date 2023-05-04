import cv2
import numpy as np
import sys
import random
from collections import deque

sys.setrecursionlimit(100000)

src = cv2.imread("Image/fable8.jpg")

# Gaussian blur 적용
blurred_src = cv2.GaussianBlur(src, (3, 3), 300)

# blurred_src = cv2.bilateralFilter(src, 9, 75, 75)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 히스토그램 평활화 적용
# equalized_gray = cv2.equalizeHist(gray)

# 전역 이진화 적용
ret, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)


def initial_sand_color():
    r = random.randint(133, 173)
    g = random.randint(82, 122)
    b = random.randint(31, 71)
    return (b, g, r)


def random_sand_color():
    r = random.randint(0, 100)
    g = random.randint(0, 40)
    b = random.randint(0, 40)
    return (b, g, r)


output = np.zeros((*binary.shape, 3), dtype=np.uint8)

height, width = binary.shape

for i in range(height):
    for j in range(width):
        output[i, j] = initial_sand_color()

visited = np.zeros_like(binary, dtype=bool)

# VideoWriter 객체 생성
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 20
video = cv2.VideoWriter("drawing_process.avi", fourcc,
                        fps, (width, height), isColor=True)


def bfs(i, j, step):
    queue = deque([(i, j)])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]

    while queue:
        i, j = queue.popleft()

        if i < 0 or i >= height or j < 0 or j >= width or visited[i, j] or binary[i, j] != 0:
            continue

        visited[i, j] = True
        # output[i, j] = random_sand_color()
        for a in range(5):
            for b in range(5):
                if i + a >= 0 and j + b >= 0 and i + a < height and j + b < width:
                    output[i + a, j + b] = random_sand_color()

        ran_show = int(random.randrange(1000, 3000))

        if ((i * j) % (ran_show)) == 0:
            cv2.imshow("output", output)
            video.write(output)  # 현재 프레임 저장
            cv2.waitKey(2)

        random.shuffle(directions)
        # step = random.randrange(1, 5)

        for dx, dy in directions:
            ni, nj = i + dx * step, j + dy * step
            if random.random() < 0.5:
                queue.append((ni, nj))
            else:
                dfs(ni, nj, step)


def dfs(i, j, step, depth=0, max_recursion_depth=1000):
    if i < 0 or i >= height or j < 0 or j >= width or visited[i, j] or binary[i, j] != 0:
        return

    visited[i, j] = True
    # output[i, j] = random_sand_color()
    flag = 0
    for a in range(3):
        for b in range(3):
            flag = random.randrange(1, 4)
            if i + a >= 0 and j + b >= 0 and i + a < height and j + b < width and flag < 3:
                output[i + a, j + b] = random_sand_color()

    ran_show = int(random.randrange(1000, 3000))

    if ((i * j) % (ran_show)) == 0:
        cv2.imshow("output", output)
        video.write(output)  # 현재 프레임 저장
        cv2.waitKey(2)

    if depth >= max_recursion_depth:
        return

    # step = random.randrange(1, 5)

    offsets = list(range(-1 * step, 2 * step, step))
    random.shuffle(offsets)

    for k in offsets:
        for l in offsets:
            ni, nj = i + k, j + l
            dfs(ni, nj, step, depth + 1, max_recursion_depth)


start_i, start_j = None, None
for i in range(0, height):
    for j in range(0, width):
        if binary[i, j] == 0 and not visited[i, j]:
            start_i, start_j = i, j
            step = 1
            if random.random() < 0.5:
                bfs(start_i, start_j, step)
            else:
                dfs(start_i, start_j, step, max_recursion_depth=10000)

# 부드러운 선을 위해 가우시안 블러 적용
output = cv2.GaussianBlur(output, (3, 3), 0)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 비디오 객체 닫기
video.release()
