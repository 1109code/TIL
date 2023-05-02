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
step = 5

dy = [-step, step, 0, 0]
dx = [0, 0, -step, step]

visited = set()

while True:
    # 시작점 찾기 (검은 픽셀 중 하나)
    start_i, start_j = None, None
    for i in range(0, height, step):
        for j in range(0, width, step):
            if binary[i, j] == 0 and (i, j) not in visited:
                start_i, start_j = i, j
                break
        if start_i is not None:
            break

    # 모든 검은 픽셀을 방문했을 경우 종료
    if start_i is None:
        break

    # 너비 우선 탐색으로 인접한 검은 픽셀 방문하기
    queue = deque([(start_i, start_j)])
    visited.add((start_i, start_j))

    while queue:
        i, j = queue.popleft()

        # 이미지를 그려나가기
        output[i:i + step, j:j + step] = binary[i:i + step, j:j + step]
        cv2.imshow("output", output)
        cv2.waitKey(1)

        for k in range(4):
            ni, nj = i + dy[k], j + dx[k]

            if 0 <= ni < height and 0 <= nj < width and (ni, nj) not in visited and binary[ni, nj] == 0:
                visited.add((ni, nj))
                queue.append((ni, nj))

cv2.waitKey(0)
cv2.destroyAllWindows()
