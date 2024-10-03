
class player():
    def __init__(self) -> None:

        self.frontal = None
        self.rightProfile = None
        self.leftProfile = None

    def getEncoders(self) -> list:
        return (self.frontal, self.rightProfile, self.leftProfile)
    
    def setFrontal(self, frontalEncoder):
        self.frontal = frontalEncoder

    def setRightProfile(self, rightEncoder):
        self.rightProfile = rightEncoder

    def setLeftProfile(self, leftEncoder):
        self.leftProfile = leftEncoder