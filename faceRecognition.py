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
    
    def addUser(self, name, surname, dni, username, gmail):
        '''
        Método encargado de añadir a un nuevo usuario con el nombre, apellido y DNI
        indicado por parametros. No contendrá características faciales hasta que el 
        usuario las añada.

        Args:
            name: Nombre del jugador
            surname: Apellidos del jugador
            dni: DNI del jugador
        '''
        newUser = player(name, surname, dni, username, gmail)

        self.players.append(newUser)

    def setFrontalEncoders(self, usuario: player, frame):
        '''
        Método encargado de calcular los Encoder para el frontal de la cara del usuario. 
        En caso de que ya se haya calculado no realiza ninguna acción. Si se detecta un
        rostro frontal en el frame, se procede al calculo de los Encoder, en caso contrario
        se descarta el frame.

        Args:
            usuario: Usuario para el cual se quiere calcular las características faciales
            frame: Frame del video que contiene la imagen del usuario
        '''
        if usuario.getFrontal() is not None:
            detection = fd.detectFrontalFace(frame)

            if detection:
                encoder = self.getNewEncoding(detection)
                usuario.setFrontal(encoder)

    def setRightProfileEncoder(self, usuario: player, frame):
        '''
        Método encargado de calcular los Encoder para el perfil derecho de la cara del usuario. 
        En caso de que ya se haya calculado no realiza ninguna acción. Si se detecta un perfil
        derecho en el frame, se procede al calculo de los Encoder, en caso contrario se descarta el frame.

        Args:
            usuario: Usuario para el cual se quiere calcular las características faciales
            frame: Frame del video que contiene la imagen del usuario
        '''
        if usuario.getRight() is not None:
            detection = fd.detectRightProfile(frame)

            if detection:
                encoder = self.getNewEncoding(detection)
                usuario.setRightProfile(encoder)

                
    def setLeftProfileEncoder(self, usuario: player, frame):
        '''
        Método encargado de calcular los Encoder para el perfil izquierdo de la cara del usuario. 
        En caso de que ya se haya calculado no realiza ninguna acción. Si se detecta un perfil
        izquierdo en el frame, se procede al calculo de los Encoder, en caso contrario se descarta el frame.

        Args:
            usuario: Usuario para el cual se quiere calcular las características faciales
            frame: Frame del video que contiene la imagen del usuario
        '''
        if usuario.getLeft() is not None:
            detection = fd.detectLeftProfile(frame)

            if detection:
                encoder = self.getNewEncoding(detection)
                usuario.setLeftProfile(encoder)