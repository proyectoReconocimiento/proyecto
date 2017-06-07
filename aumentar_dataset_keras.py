import keras
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True)

source = ""
destiny = ""

#para las de plastico
generador = datagen.flow_from_directory(source, classes=['plastico'], save_to_dir=destiny+"/plastico", save_format="JPEG",save_prefix="auto" )
i = 0
for batch in generador:
    i += 1
    if i > 10: # voy a guardar solo 10 * 32 imagenes (640)
        break  # si no el generador no pararia nunca

# para las de vidrio
generador2 = datagen.flow_from_directory(source,classes=['vidrio'], save_to_dir=destiny+"/vidrio", save_format="JPEG", save_prefix="auto")
i = 0
for batch in generador2:
    i += 1
    if i > 10:
        break

