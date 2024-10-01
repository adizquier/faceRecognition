import cv2
import os

if not os.path.exists("faces"):
     os.makedirs("faces")

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")