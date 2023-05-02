import cv2
import numpy as np


def dfs(img, x, y):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if 0 <= x < img.shape[1] and 0 <= y < img.shape[0] and img[y, x] == 255:
            img[y, x] = 0

            stack.append((x - 1, y))
            stack.append((x + 1, y))
            stack.append((x, y - 1))
            stack.append((x, y + 1))
            cv2.imshow("output", output)
            cv2.waitKey(1)


src = cv2.imread("Image/fable.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 467, 37)

# 외곽선 검출
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 빈 output 이미지 생성 (흰색)
output = np.full(binary.shape, 255, dtype=np.uint8)

# 이미지의 높이와 너비
height, width = binary.shape

# 점진적으로 이미지를 보여주는 단위 설정
step = 1

# 샌드 아트처럼 그리기
for i, contour in enumerate(contours):
    if hierarchy[0][i][3] == -1:  # 최상위 계층의 외곽선만 그림
        for point in contour:
            x, y = point[0][0], point[0][1]
            output[y:y + step, x:x + step] = 0
            cv2.imshow("output", output)
            cv2.waitKey(1)  # 그리기 속도 조절

# DFS로 내부 채우기
starting_point = (width // 2, height // 2)  # 이미지 중앙을 시작점으로 설정
dfs(output, starting_point[0], starting_point[1])

cv2.imshow("output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
