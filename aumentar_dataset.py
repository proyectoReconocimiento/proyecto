from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
import scipy.misc
import os
import cv2

def rotar_y_guardar(image, i, destiny):
    (h, w) = image.shape[:2]
    (cX, cY) = (w / 2, h / 2)

    M3 = cv2.getRotationMatrix2D((cX, cY), -45, 1.0)
    rotada = cv2.warpAffine(image, M3, (w, h))
    #la imagen se guardara con el nombre nom, por ejemplo auxRot0.jpeg cuando le pasemos i = 0
    nom = destiny + "/auxRot" + `i` + ".jpeg"
    scipy.misc.imsave(nom, rotada)

def voltear_y_guardar(image, i, destiny):
    volteadoHV = cv2.flip(image, -1)
    #la imagen se guardara con el nombre nom, por ejemplo auxVol0.jpeg cuando le pasemos i = 0
    nom = destiny + "/auxVol" + `i` + ".jpeg"
    scipy.misc.imsave(nom, volteadoHV)

source = ""
destiny = ""

i=0

for file in os.listdir(source):
    image = cv2.imread(source+"/"+file)
    # la siguiente invocación rota y guarda la imagen
    rotar_y_guardar(image, i, destiny)

    # la siguiente voltea y guarda la imagen
    voltear_y_guardar(image, i, destiny)

    i+=1

