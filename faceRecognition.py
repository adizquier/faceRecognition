import cv2
import numpy as np
import os
import face_recognition
import matplotlib.pyplot as plt

FACES_DIR = './faces/'

facesEncodings = []
facesNames = []


# Cargar las imágenes de las caras y sus codificaciones
for fileName in os.listdir(FACES_DIR):
    image = cv2.imread(os.path.join(FACES_DIR, fileName))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Cambiar a RGB

    # La tupla indica que las coordenadas de la imagen de la cara comienzan en (0,0) y finalizan en (150, 150)
    f_coding = face_recognition.face_encodings(image, known_face_locations=[(0, 150, 150, 0)])[0]
    facesEncodings.append(f_coding)
    facesNames.append(fileName.split(".")[0])


# Inicializa la captura de video. Modificar indice segun la camara
cap = cv2.VideoCapture(2)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

plt.ion()  # Activa el modo interactivo de matplotlib
fig, ax = plt.subplots()  # Crea una figura y ejes para mostrar la imagen

while True:
    ret, frame = cap.read()
    if not ret or frame is None or not np.any(frame):  # Verifica si el frame está vacío o negro
        print("Error: No se puede capturar la imagen o el frame está vacío.")
        break

    frame = cv2.flip(frame, 1)
    orig = frame.copy()
    faces = faceClassif.detectMultiScale(frame, 1.1, 5)

    for (x, y, w, h) in faces:
        face = orig[y:y + h, x:x + w]
        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)  # Cambiar a RGB

        actual_face_encoding = face_recognition.face_encodings(face)

        # Solo continúa si se encuentra un encoding
        if actual_face_encoding:
            actual_face_encoding = actual_face_encoding[0]
            result = face_recognition.compare_faces(facesEncodings, actual_face_encoding)

            if True in result:
                index = result.index(True)
                name = facesNames[index]
                color = (125, 220, 0)
            else:
                name = "Desconocido"
                color = (50, 50, 255)

            # Dibuja un rectángulo y el nombre
            cv2.rectangle(frame, (x, y + h), (x + w, y + h + 30), color, -1)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, name, (x, y + h + 25), 2, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Convierte la imagen a RGB para matplotlib
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Muestra la imagen usando matplotlib
    ax.clear()  # Limpiar los ejes
    ax.imshow(frame_rgb)
    ax.axis('off')  # Opcional: ocultar los ejes
    plt.pause(0.001)  # Pausa para permitir que se actualice la figura

    # Rompe el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
plt.close(fig)  # Cierra la figura de matplotlib
cv2.destroyAllWindows()
