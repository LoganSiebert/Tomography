from skimage.io import imread #Importe la fct qui va lire l'image
from skimage.transform import radon, iradon, resize #Importe la fonction qui va effectuer la transformée
import numpy as np
import matplotlib.pyplot as plt #Pour le graphique
from math import log

fichier=open('C:\\Users\\Mathieu\\Desktop\\SimulationTomographie\\simulneuf.txt','r')
valeurs=fichier.readlines()

for i in range(len(valeurs)):
    valeurs[i]=int(valeurs[i][:4])

theta=theta=np.linspace(0,180,18)

image=[]

for i in range(10):
    image.append([])

for i in range(10):
    for j in range(9):
        image[i].append(valeurs[18*i+2*j]-10)
        image[i].append(valeurs[18*(9-i)+(2*j+1)]-10)

I0=1002
mu=0.9
for i in image:
    for j in range(len(i)):
        i[j]=-log(i[j]/I0)/mu
        
sinogramme=np.array(image)
print(sinogramme.shape)
image_rebuild=iradon(sinogramme,theta,circle=True)
print(image_rebuild.shape)
plt.imshow(image_rebuild, cmap=plt.cm.Greys_r)
plt.show()
