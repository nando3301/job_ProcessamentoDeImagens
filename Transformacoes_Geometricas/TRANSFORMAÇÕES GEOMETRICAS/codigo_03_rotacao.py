# -*- coding: cp1252 -*-
import cv2
import numpy as np
#from matplotlib import pyplot as plt


imgOriginal = cv2.imread('C:\\Users\\Fernando\\Desktop\\job_p_imagens\\gof_01.jpg',0)
res = cv2.resize(imgOriginal, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)


totalLinhas, totalColunas = res.shape

matriz = cv2.getRotationMatrix2D((totalColunas/2, totalLinhas/2), 45,1)

imgRotacionada = cv2.warpAffine(res, matriz, (totalColunas, totalLinhas))


cv2.imshow("Imagem rotacionada 45", imgRotacionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
