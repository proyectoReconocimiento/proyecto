from __future__ import print_function
from pyimagesearch.utils import Conf
import numpy as np
import argparse
import cPickle
import h5py
import cv2
import sys
from pyimagesearch.overfeat import GoogleNetExtractor

def prepare_image(image, fixedSize):
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	image = cv2.resize(image, tuple(fixedSize))
	return image

# construct the argument parser and parse the command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required=True, help="path to configuration file")
ap.add_argument("-i", "--image", required=True, help="path to image")
args = vars(ap.parse_args())
path=args["image"]
# load the configuration, label encoder, and classifier
print("[INFO] loading model...")
conf = Conf(args["conf"])
fixedSize = conf["overfeat_fixed_size"]
le = cPickle.loads(open(conf["label_encoder_path"]).read())
model = cPickle.loads(open(conf["classifier_path"]).read())


image = prepare_image(cv2.imread(path), fixedSize)
image = np.array(image, dtype="float")
oe = GoogleNetExtractor()
features = oe.describe(image)
# classify the vector
prediction = model.predict(np.atleast_2d(features))[0]
prediction = le.inverse_transform(prediction)

# load the image, draw the prediction on it, and display it
# this is how de model sees the image
cv2.imshow("Image", image)
cv2.waitKey(0)
# And this is the original image with the prediction written on it
imagenOriginal=cv2.imread(path)
cv2.putText(imagenOriginal, prediction, (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
	(0, 255, 0), 3)

cv2.imshow("Image", imagenOriginal)
cv2.waitKey(0)

