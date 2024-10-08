import cv2

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
profileClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")

def draw_detection(detection, dest_image):
     '''
     Método encargado de dibujar una detección

     Args:
          detection: Detección realizada
          dest_image: Imagen destino sobre la que se dibujará
     '''
     if(detection is not None):
          x, y, w, h = detection
          color = (0, 255, 255)
          stroke = 5
          cv2.rectangle(dest_image, (x, y), (x + w, y + h), color, stroke)

def select_biggest_detection(detections):
     '''
     Metodo encargado de seleccionar la deteccion mas grande de todas las detecciones, es decir,
     la que corresponde a la deteccion más cercana a la cámara.

     Args:
          detections: Lista que contiene todas las detecciones 
     
     Returns:
          biggest: Detección más cercana a la cámara
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

     Returns:
          bigestFace: Frontal de la cara detectado más cercano a la cámara
          None: Si no se ha detectado nada en el frame
     '''

     faces = faceClassif.detectMultiScale(image, 1.1, 5)

     if len(faces) != 0:

          face = select_biggest_detection(faces)
          x, y, w, h = face

          bigestFace = image[y:y + h, x:x + w]

          return bigestFace
     
     return None

def detectLeftProfile(image):
     '''
     Método encargado de realizar la detección de perfiles izquierdos

     Args:
          image: Imagen sobre la cual se realizará la detección
     
     Returns:
          bigestProfile: Perfil izquierdo más cercano a la cámara
          None: Si no se ha detectado nada sobre el frame
     '''
     profiles = profileClassif.detectMultiScale(image, 1.1, 5)

     if len(profiles) != 0:

          prof = select_biggest_detection(profiles)
          x, y, w, h = prof

          bigestProfile = image[y:y + h, x:x + w]

          return bigestProfile
     
     return None

def detectRightProfile(image):
     '''
     Método encargado de realizar la detección de perfiles derechos

     Args:
          image: Imagen sobre la cual se realizará la detección

     Returns:
          bigestProfile: Perfil derecho más cercano a la cámara
          None: Si no se ha detectado nada sobre el frame
     '''
     image = cv2.flip(image, 1)

     profiles = profileClassif.detectMultiScale(image, 1.1, 5)

     if len(profiles) != 0:

          prof = select_biggest_detection(profiles)
          x, y, w, h = prof

          bigestProfile = image[y:y + h, x:x + w]

          return bigestProfile
     
     return None

    