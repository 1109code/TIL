# import cv2
# print(cv2.__version__)

import numpy as np
import cv2

image = cv2.imread("Image/son.jpg", cv2.IMREAD_UNCHANGED)

cv2.imshow("Son", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
