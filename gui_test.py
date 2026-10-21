import cv2
import numpy as np

print("Starting GUI test...")

img = np.zeros((480, 640, 3), dtype=np.uint8)

cv2.namedWindow("GUI Test", cv2.WINDOW_NORMAL)
cv2.imshow("GUI Test", img)

print("Window created. Press any key inside the window.")

cv2.waitKey(0)

cv2.destroyAllWindows()

print("GUI test finished.")