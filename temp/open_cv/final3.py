import cv2
import numpy as np
import sys
import random
from collections import deque
from PIL import Image
import imageio

sys.setrecursionlimit(100000)

src = cv2.imread("Image/fable7.jpg")

# Gaussian blur 적용
blurred_src = cv2.GaussianBlur(src, (3, 3), 300)

gray = cv2.cvtColor(blurred_src, cv2.COLOR_BGR2GRAY)

# 히스토그램 평활화 적용
equalized_gray = cv2.equalizeHist(gray)

# 전역 이진화 적용
ret, binary = cv2.threshold(equalized_gray, 128, 255, cv2.THRESH_BINARY)


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

# VideoWriter 객체 생성
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 20
video = cv2.VideoWriter("drawing_process.avi", fourcc,
                        fps, (width, height), isColor=True)

frames = []  # 프레임 저장을 위한 리스트 생성


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
            # 현재 프레임을 RGB 형식으로 변환하여 저장
            frames.append(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
            cv2.waitKey(10)

        random.shuffle(directions)

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
    output[i, j] = random_sand_color()

    ran_show = int(random.randrange(5000, 10000))

    if ((i * j) % (ran_show)) == 0:
        cv2.imshow("output", output)
        # 현재 프레임을 RGB 형식으로 변환하여 저장
        frames.append(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
        cv2.waitKey(10)

    if depth >= max_recursion_depth:
        return

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

# 프레임 리스트를 GIF로 저장
duration = 1000 / fps
frames_pil = []

for frame in frames:
    pil_img = Image.fromarray(frame)
    pil_img = pil_img.convert('P', palette=Image.ADAPTIVE)
    frames_pil.append(pil_img)

frames_pil[0].save('drawing_process.gif', format='GIF',
                   append_images=frames_pil[1:], save_all=True, duration=duration, loop=0)