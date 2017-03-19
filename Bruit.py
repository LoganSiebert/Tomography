#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from skimage.io import imread #Importe la fct qui va lire l'image
from skimage.transform import downscale_local_mean, radon, iradon, resize #Importe la fonction qui va effectuer la transformée
import numpy as np
import matplotlib.pyplot as plt #Pour le graphique


image=imread("C:\\Users\\Mathieu\\Desktop\\SimulationTomographie\\imagetest.jpg",as_grey=True)
theta=np.linspace(0,180,100)

sinogramme=radon(image,theta)
#print(sinogramme.shape)
image2=iradon(sinogramme, theta, circle=False)
sinogramme=sinogramme.tolist()

for i in sinogramme:
    for j in range(100):
        #i[j-1]=i[j-1]+random.gauss(0,3.5)
        i[j-1]=i[j-1]+random.uniform(-5,5)

sinogramme=np.array(sinogramme)





#Transformée inverse
image_rebuild = iradon(sinogramme, theta, circle=False)
plot_image = np.concatenate((image_rebuild, image2, image), axis=1)
plt.imshow(plot_image, cmap=plt.cm.Greys_r)

plt.show()
