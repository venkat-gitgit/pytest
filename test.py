import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('IMG.jpg')
layer = img.copy
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i),layer)

cv2.imshow('upper level gau pyr',gp[5]) 
plt.savefig('pyramid_laplacian.png',bbox_inches='tight')

for i in range(5,0,-1):
    gaussion_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussion_extended)
    # cv2.imshow(str(i),laplacian)
    plt.savefig("lap_"+str(i)+".jpg",laplacian)

plt.savefig('pyramid_laplacian.png',bbox_inches='tight')