
class melodie:
    
    def __init__(self, titlu, artist, gen, data):
        self.__titlu = titlu
        self.__artist = artist
        self.__gen = gen
        self.__data = data
        
    #getters
    def getTitlu(self):
        return self.__titlu

    def getArtist(self):
        return self.__artist

    def getGen(self):
        return self.__gen

    def getData(self):
        return self.__data

    #setters
    def setTitlu(self,attr):
        self.__titlu = attr

    def setArtist(self,attr):
        self.__artist = attr

    def setGen(self,attr):
        self.__gen = attr

    def setData(self,attr):
        self.__data = attr
        
    def fileFormat(self):
        """Formatul de memorare in fisier al entitatii
        """
        return "{};{};{};{};\n".format(self.__titlu, self.__artist, self.__gen, self.__data)
    
    def __str__(self):
        """Formatul de afisare in export-uri + consola
        """
        return "{},{},{},{}\n".format(self.__titlu, self.__artist, self.__data, self.__gen, )