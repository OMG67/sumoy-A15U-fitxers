class Videogame:
    #Constructor
    #Used to create attributes for the class
    def __init__(self, _name, _desc, _gen, _dev, _price):
        self.listGames = []
        self.name = _name
        self.desc = _desc
        self.genre = _gen
        self.dev = _dev
        self.price = _price

    #Mètodes
    #Setters
    #Used to assign a value to an attribute of the class
    def setName(self, _name):
        self.name = _name
    def setDescription(self, _desc):
        self.desc = _desc
    def setGenre(self, _gen):
        self.genre = _gen
    def setDeveloper(self, _dev):
        self.dev = _dev
    def setPrice(self, _price):
        self.price = _price
    
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