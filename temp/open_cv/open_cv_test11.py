import cv2
import numpy as np

src = cv2.imread("Image/fable.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 467, 37)

# 외곽선 검출
edges = cv2.Canny(gray, 100, 200)

# 빈 output 이미지 생성 (흰색)
output = np.full(binary.shape, 255, dtype=np.uint8)

# 이미지의 높이와 너비
height, width = binary.shape

# 점진적으로 이미지를 보여주는 단위 설정
step = 5

# 외곽선을 그리는 과정 보여주기
for i in range(0, height, step):
    for j in range(0, width, step):
        if edges[i, j] > 0:
            output[i:i + step, j:j + step] = 0
            cv2.imshow("output", output)
            cv2.waitKey(1)

# 외곽선을 그린 후 내부를 랜덤으로 채우기
for i in range(0, height, step):
    for j in range(0, width, step):
        if binary[i, j] == 0 and output[i, j] != 0:
            output[i:i + step, j:j + step] = 0
            cv2.imshow("output", output)
            cv2.waitKey(1)

cv2.waitKey(0)
cv2.destroyAllWindows()
