# -*- coding: cp1252 -*-
import cv2
import numpy as np

imgOriginal = cv2.imread('C:\\Users\\Fernando\\Desktop\\job_p_imagens\\gof_01.jpg',0)

imgModificada = cv2.resize(imgOriginal, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)

cv2.imshow("Imagem original", imgOriginal)
cv2.imshow("Imagem modificada", imgModificada)
cv2.waitKey(0)
cv2.destroyAllWindows()

