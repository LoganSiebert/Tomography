#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from skimage.io import imread #Importe la fct qui va lire l'image
from skimage.transform import downscale_local_mean, radon, iradon, resize #Importe la fonction qui va effectuer la transformée
import numpy as np
import matplotlib.pyplot as plt #Pour le graphique
liste_theta=[]
liste_images=[]
for i in range(20):
    liste_theta.append(np.linspace(0,360,(i+1)*10))

image=imread("C:\\Users\\Mathieu\\Desktop\\SimulationTomographie\\imagetest.jpg",as_grey=True)

for i in range(20):
    liste_images.append(radon(image,liste_theta[i]))

for i in range(20):
    liste_images[i] = iradon(liste_images[i],liste_theta[i],circle=False)

liste_images.append(image)

for i in range(21):
    plt.imshow(liste_images[i])
    plt.figure(i+1)


plt.show()
