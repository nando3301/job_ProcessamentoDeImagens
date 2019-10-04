# -*- coding: cp1252 -*-
import cv2
import numpy as np

imgOriginal = cv2.imread('C:\\Users\\Fernando\\Desktop\\job_p_imagens\\gof_02.jpg',0)
totalLinhas, totalColunas = imgOriginal.shape[:2]
res = cv2.resize(imgOriginal, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

matriz = np.float32([[1,0,100],[0,1,100]])

imgDeslocada = cv2.warpAffine(res, matriz, (totalColunas, totalLinhas))

cv2.imshow("Imagem Deslocada", imgDeslocada)
cv2.waitKey(0)
cv2.destroyAllWindows()



                    
