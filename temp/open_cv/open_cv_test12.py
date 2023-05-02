import cv2
import numpy as np

src = cv2.imread("Image/fable.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 467, 37)

# 외곽선 검출
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 빈 output 이미지 생성 (흰색)
output = np.full(binary.shape, 255, dtype=np.uint8)

# 이미지의 높이와 너비
height, width = binary.shape

# 점진적으로 이미지를 보여주는 단위 설정
step = 5

# 샌드 아트처럼 그리기
for contour in contours:
    for point in contour:
        x, y = point[0][0], point[0][1]
        output[y:y + step, x:x + step] = 0
        cv2.imshow("output", output)
        cv2.waitKey(1)  # 그리기 속도 조절

# 외곽선을 채우기
cv2.drawContours(output, contours, -1, (0, 0, 0), -1)

cv2.imshow("output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
