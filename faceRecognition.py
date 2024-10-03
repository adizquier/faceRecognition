import faceDetection as fd
import face_recognition
from player import player


class faceRecognition():

    def __init__(self) -> None:
        self.players: list[player] = []

    def getNewEncoding(self, image):
        '''
        Método encargado de calcular un nuevo Encoding del rostro pasado por parámetros

        Args:
            image: Imagen del rostro sobre la cual se calcularán los Encodings
        Returns:
            f_coding: Encodings calculados para el rostro
        '''
        f_coding = face_recognition.face_encodings(image, known_face_locations=[(0, 150, 150, 0)])[0]
        
        return f_coding
    
    def compareEncodings(self, image):
        '''
        Método encargado de calcular los Encodings sobre un rostro detectado y comprobar si se corresponde
        a un usuario registrado o no

        Args:
            image: Imagen que contiene el rostro detectado
        Returns:
            bool: True si el rostro detectado pertenece a una persona registrada, False en caso contrario

        '''
        f_coding = face_recognition.face_encodings(image)

        for player in self.players:
            encoders = player.getEncoders()

            result = face_recognition.compare_faces(encoders, f_coding)

            if result: return True
        
        return False
    
    def addUser(self, name):
        '''
        Método encargado de añadir a un usuario. Se encargará de obtener el frontal de la cara, el perfil derecho e izquierdo para 
        posteriormente almacenarlos en el diccionario de Encodings con la clave que el usuario introduzca.
        '''
        newUser = player(name)