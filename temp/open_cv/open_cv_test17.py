import cv2
import numpy as np

src = cv2.imread("Image/fable2.jpg")
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

# 내부를 점진적으로 채우기
fill_step = 5
for y in range(0, height, fill_step):
    for x in range(0, width, fill_step):
        is_inside = False
        for contour in contours:
            if cv2.pointPolygonTest(contour, (x, y), False) >= 0:
                is_inside = True
                break
        if is_inside:
            output[y:y + fill_step, x:x + fill_step] = 0
            cv2.imshow("output", output)
            cv2.waitKey(1)  # 빠르게 채우기

cv2.imshow("output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
