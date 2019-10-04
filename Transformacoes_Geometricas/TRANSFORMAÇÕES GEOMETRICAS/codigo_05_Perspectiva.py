import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:\\Users\\Fernando\\Desktop\\job_p_imagens\\gof.jpg',0)
res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

rows,cols = res.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(res,M,(300,300))

plt.subplot(121),plt.imshow(res),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
