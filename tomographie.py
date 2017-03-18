import serial
from skimage.io import imread #Importe la fct qui va lire l'image
from skimage.transform import radon, iradon, resize #Importe la fonction qui va effectuer la transformée
import numpy as np
import matplotlib.pyplot as plt #Pour le graphique


def tomographie() :
    ser = serial.Serial(port = "COM1", baudrate = 9600)
    ser.open()
    Process = True
    
    if not ser.isOpen():
        print ("Erreur d'ouverture du port !")
        exit(1)
	
    fichier = open('output.txt', 'w')

#if not fichier:
#print "Erreur d'ouverture du fichier !"
#exit(1)
    summ = 0
    try:
        for i in range(9) :
            summ = summ +int(ser.readline())
        summ = summ * 0.1
            
        while Process == True :
        
            if int(fichier.readline()) != -10 :
                line = ser.readline()
                fichier.write(line)
            else :
                Process == False
	
    except (KeyboardInterrupt, SystemExit):
        ser.close()
        fichier.close()
    except:
        print ("Erreur interne !")
    process = True
    matrix=[range(200)*200]
    I_0 = 1012
    mu = 0.9
    while process==True:
        for i in range(200):
            for j in matrix[i]:
                data = int(fichier.readline())- summ #the last bit gets rid of the new-line chars
                x = - log(data/I_0)/mu
                matrix[i][j] = x
                j+=1
            i+=1

    return np.array(matrix)

sinogramm = tomographie()

    #image = resize(image,(2000,2000))

    #Transformée de radon
theta = np.linspace(0., 180., 50, endpoint=False)
    #sinogram = radon(image, theta)

    #Affichage
    #plt.imshow(sinogram, cmap=plt.cm.Greys_r)

    #Transformée inverse
image_rebuild = iradon(sinogram, theta)
plt.imshow(image_rebuild, cmap=plt.cm.Greys_r)

plt.show()
