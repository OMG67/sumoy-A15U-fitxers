class Developer:
    #Constructor
    #Used to create attributes for the class
    def __init__(self, _name, _ceo, _networth, _location):
        self.listGames = []
        self.name = _name
        self.ceo = _ceo
        self.net = _networth
        self.location = _location

    #Mètodes
    #Setters
    #Used to assign a value to an attribute of the class
    def setName(self, _name):
        self.name = _name
    def setCeo(self, _ceo):
        self.desc = _ceo
    def setNetworth(self, _networth):
        self.genre = _networth
    def setLocation(self, _location):
        self.dev = _location
    
    #Getters
    #Used to get info out of an attribute of the class
    def getName(self):
        return self.name
    def getDescription(self):
        return self.desc
    def getGenre(self):
        return self.genre
    def getDeveloper(self):
        return self.dev
    def getPrice(self):
        return self.price