import glob, os
from PIL import Image
import cv2
import sys
import shutil
size = 128, 128

#origen indica el directorio donde se encuentran las imagenes que queremos filtrar
origen = ""

#indicamos tantos destinos como clasificaciones queremos hacer
destino1=""
destino2=""
# destino3=""
# destino4=""
# destino5=""
# destino6=""
# destino7=""
# destino8=""

#indicamos la tecla que debemos pulsar para mandar una imagen a un destino en concreto
teclaDestino1 = ord('')
teclaDestino2 = ord('')
# teclaDestino3 = ord('')
# teclaDestino4 = ord('')
# teclaDestino5 = ord('')
# teclaDestino6 = ord('')
# teclaDestino7 = ord('')
# teclaDestino8 = ord('')

for file in os.listdir(origen):
    image = cv2.imread(origen + "/" + file)
    print file
    cv2.imshow("", image)
    tecla = cv2.waitKey(0)
    if tecla == teclaDestino1:
        shutil.move(origen + "/" + file, destino1)
    elif tecla == teclaDestino2:
        shutil.move(origen + "/" + file, destino2)
    # elif tecla == teclaDestino3:
    #     shutil.move(origen + "/" + file, destino3)
    # elif tecla == teclaDestino4:
    #     shutil.move(origen + "/" + file, destino4)
    # elif tecla == teclaDestino5:
    #     shutil.move(origen + "/" + file, destino5)
    # elif tecla == teclaDestino6:
    #     shutil.move(origen + "/" + file, destino6)
    # elif tecla == teclaDestino7:
    #     shutil.move(origen + "/" + file, destino7)
    # elif tecla == teclaDestino8:
    #     shutil.move(origen + "/" + file, destino8)