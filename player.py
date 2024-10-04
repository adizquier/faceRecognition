
class player():
    def __init__(self, name = "", surname = "", dni = "", username = "", gmail = "") -> None:

        self.name = name
        self.surnames = surname
        self.DNI = dni
        self.username = username
        self.gmail = gmail

        self.frontal = None
        self.rightProfile = None
        self.leftProfile = None

    def getName(self):
        return self.name
    
    def getSurname(self):
        return self.surnames
    
    def getDNI(self):
        return self.DNI
    
    def getUserName(self):
        return self.username
    
    def getGmail(self):
        return self.gmail

    def getEncoders(self) -> list:
        return (self.frontal, self.rightProfile, self.leftProfile)
    
    def getFrontal(self):
        return self.frontal
    
    def getLeft(self):
        return self.leftProfile
    
    def getRight(self):
        return self.rightProfile
    
    def setFrontal(self, frontalEncoder):
        self.frontal = frontalEncoder

    def setRightProfile(self, rightEncoder):
        self.rightProfile = rightEncoder

    def setLeftProfile(self, leftEncoder):
        self.leftProfile = leftEncoder