#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from skimage.io import imread #Importe la fct qui va lire l'image
from skimage.transform import downscale_local_mean, radon, iradon, resize #Importe la fonction qui va effectuer la transformée
import numpy as np
import matplotlib.pyplot as plt #Pour le graphique






image=imread("C:\\Users\\Mathieu\\Desktop\\SimulationTomographie\\imagetest.jpg",as_grey=True)
theta=np.linspace(0,360,32)
#image2=downscale_local_mean(image,(8,8))
image2=resize(image,(100,100))

sinogramme=radon(image2,theta)

#Bruit
#sinogramme=sinogramme.tolist()
#for i in sinogramme:
#    for j in range(32):
#        i[j-1]=i[j-1]+random.gauss(0,0)
#sinogramme=np.array(sinogramme)



#Transformée inverse
image_rebuild = iradon(sinogramme, theta, circle=False)
liste_images=[image,image2,image_rebuild,image]
for i in range(4):
    plt.imshow(liste_images[i])
    plt.figure(i+1)

plt.show()
