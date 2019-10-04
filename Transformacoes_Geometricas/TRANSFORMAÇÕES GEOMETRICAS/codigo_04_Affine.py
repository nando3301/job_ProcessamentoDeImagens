import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:\\Users\\Fernando\\Desktop\\job_p_imagens\\gof_01.jpg',0)
res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
rows,cols = res.shape


pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(res,M,(cols,rows))

plt.subplot(121),plt.imshow(res),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
