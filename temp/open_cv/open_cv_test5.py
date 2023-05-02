import cv2
import numpy as np
import random

src = cv2.imread("Image/son.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 467, 37)

# 빈 output 이미지 생성 (검은색)
# output = np.zeros_like(binary)

# 빈 output 이미지 생성 (흰색)
output = np.full(binary.shape, 255, dtype=np.uint8)

# 이미지의 높이와 너비
height, width = binary.shape

# 점진적으로 이미지를 보여주는 단위 설정 (예: 20픽셀)
step = 5

# 이미지를 랜덤하게 표시할 횟수 설정
iterations = int(height * width / (step * step))
print(iterations)

for _ in range(iterations):
    # 랜덤한 위치 선택
    i = random.randint(0, height - step)
    j = random.randint(0, width - step)

    # 원본 이미지에서 일부분을 추출
    partial_binary = binary[i:i + step, j:j + step]

    # 출력 이미지에 해당 부분을 덧붙임
    output[i:i + step, j:j + step] = partial_binary

    # 결과 이미지를 보여줌
    cv2.imshow("output", output)
    cv2.waitKey(1)  # 각 단계별로 100ms 대기

cv2.waitKey(0)
cv2.destroyAllWindows()
