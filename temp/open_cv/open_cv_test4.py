import cv2
import numpy as np

src = cv2.imread("Image/son.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 467, 37)

# 빈 output 이미지 생성 (검은색)
output = np.zeros_like(binary)

# 이미지의 높이와 너비
height, width = binary.shape

# 점진적으로 이미지를 보여주는 단위 설정 (예: 20픽셀)
step = 20

for i in range(0, height, step):
    for j in range(0, width, step):
        # 원본 이미지에서 일부분을 추출
        partial_binary = binary[i:i+step, j:j+step]

        # 출력 이미지에 해당 부분을 덧붙임
        output[i:i+step, j:j+step] = partial_binary

        # 결과 이미지를 보여줌
        cv2.imshow("output", output)
        cv2.waitKey(100)  # 각 단계별로 100ms 대기

cv2.waitKey(0)
cv2.destroyAllWindows()
