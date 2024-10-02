import cv2


IMG_DIR = './images/'

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
profileClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")


def select_biggest_detection(detections):
     '''
     Metodo encargado de seleccionar la deteccion mas grande de todas las detecciones, es decir,
     la que corresponde a la deteccion más cercana a la cámara.

     Args:
          detections: Lista que contiene todas las detecciones 
     '''     
     maxArea = 0
     biggest = None

     for(x, y, w, h) in detections:
          if w*h > maxArea:
               maxArea = w*h
               biggest = (x, y, w, h)

     return biggest       

def detectFrontalFace(image):
     '''
     Metodo encargado de realizar detecciones de rostros frontales en una imagen

     Args:
          image: Imagen sobre la cual se realizará la detección
     '''

     faces = faceClassif.detectMultiScale(image, 1.1, 5)

     face = select_biggest_detection(faces)
     x, y, w, h = face

     bigestFace = image[y:y + h, x:x + w]
     bigestFace = cv2.resize(face, (150, 150))

     return bigestFace

def detectLeftProfile(image):
     '''
     Método encargado de realizar la detección de perfiles izquierdos

     Args:
          image: Imagen sobre la cual se realizará la detección
     '''
     profiles = profileClassif.detectMultiScale(image, 1.1, 5)

     prof = select_biggest_detection(profiles)
     x, y, w, h = prof

     bigestProfile = image[y:y + h, x:x + w]
     bigestProfile = cv2.resize(prof, (150, 150))   

     return bigestProfile

def detectRightProfile(image):
     '''
     Método encargado de realizar la detección de perfiles derechos

     Args:
          image: Imagen sobre la cual se realizará la detección
     '''
     image = cv2.flip(image, 1)
     
     profiles = profileClassif.detectMultiScale(image, 1.1, 5)

     prof = select_biggest_detection(profiles)
     x, y, w, h = prof

     bigestProfile = image[y:y + h, x:x + w]
     bigestProfile = cv2.resize(prof, (150, 150))   

     return bigestProfile

    