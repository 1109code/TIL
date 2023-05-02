import cv2
import numpy as np

src = cv2.imread("Image/fable.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 467, 37)

# 빈 output 이미지 생성 (흰색)
output = np.full(binary.shape, 255, dtype=np.uint8)

# 이미지의 높이와 너비
height, width = binary.shape

# 점진적으로 이미지를 보여주는 단위 설정
step = 3

dy = [-step, step, 0, 0]
dx = [0, 0, -step, step]

visited = np.zeros_like(binary, dtype=bool)


def dfs(i, j):
    if i < 0 or i >= height or j < 0 or j >= width or visited[i, j] or binary[i, j] == 255:
        return

    visited[i, j] = True
    output[i:i + step, j:j + step] = binary[i:i + step, j:j + step]
    cv2.imshow("output", output)
    cv2.waitKey(1)

    # 모든 방향으로 이동
    for k in range(4):
        ni, nj = i + dy[k], j + dx[k]
        dfs(ni, nj)

    # 현재 위치에서 추가로 이동할 수 있는 경우에 대해 재귀 호출을 수행
    for k in range(4):
        ni, nj = i + dy[k], j + dx[k]
        if 0 <= ni < height and 0 <= nj < width and not visited[ni, nj] and binary[ni, nj] == 0:
            dfs(ni, nj)


# 시작점 찾기 (검은 픽셀 중 하나)
start_i, start_j = None, None
for i in range(0, height, step):
    for j in range(0, width, step):
        if binary[i, j] == 0 and not visited[i, j]:
            start_i, start_j = i, j
            dfs(start_i, start_j)

cv2.waitKey(0)
cv2.destroyAllWindows()
