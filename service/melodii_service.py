from email import generator
from multiprocessing.sharedctypes import Value
from repository.melodii_repo import melodii_repo
from entities.melodie import melodie
from validators.melodii_validator import validator
from generators.generator import generator
from datetime import date


def convert_data(data):
    data = data.split('/')
    data = date(int(data[2]), int(data[1]), int(data[0]))
    
    return data

def key_sort(ent:melodie):
    data  = ent.getData()
    data = convert_data(data)
    
    return data


class melodii_service:
    def __init__(self, testing = False):
        if testing:
            self.__repo = melodii_repo('test')
        else:
            self.__repo = melodii_repo()
        self.__validator = validator()
        self.__generator = generator()
    
    def getAll(self):
        return self.__repo.getAll()
    
    def addMelodie(self, titlu, artist, gen, data):
        """Verifica validitatea datelor transmise si adauga o melodie in fisier
        

        Args:
            titlu (str): titlul melodiei
            artist (str): autorul melodiei
            gen (str): genul melodiei
            data (str): data melodiei

        Raises:
            ValueError: Lungime titlu si artist vida
            error: eroare la gen sau data
        """
        try:
            self.__validator.validate(gen, data)
            if len(titlu)==0 or len(artist)==0:
                raise ValueError("Lungime artist/titlu vida")
        except ValueError as error:
            raise error
        
        self.__repo.uploadOneElem(melodie(titlu, artist, gen, data))
        
    def searchElem(self, titlu, artist):
        """Returneaza indexul la care melodia 
        cu titlu si artist poate fi gasit

        Args:
            titlu (string): titlul melodiei
            artist (string): autorul melodiei 

        Returns:
            int: index-ul din fisiser al melodiei
        
        Raises:

        """
        ent_lst = self.__repo.getAll()
        
        index = -1
        for i,ent in enumerate(ent_lst):
            if ent.getTitlu() == titlu and ent.getArtist() == artist:
                index = i
                
        if index == -1:
            raise ValueError("Nu exista melodie.")
        else:
            return index
        
    
        
    def modifElem(self,index , gen, data):
        """Modifica elementul pe pozitia 'index'

        Args:
            index (int): pozitia elementului de modificat
            gen (str): genul de modificat
            data (str): data de modificat

        Raises:
            error: Eroare la datele introduse( gen, data)
            ValueError: Eroare la indexul introdus.
        """
        try:
            self.__validator.validate(gen, data)
        except ValueError as error:
            raise error
        
        ent_lst = self.__repo.getAll()
        
        if index>=len(ent_lst):
            raise ValueError("Index gresit.")
        else:
            ent_lst[index].setGen(gen)
            ent_lst[index].setData(data)
            self.__repo.uploadList(ent_lst)
            
    def genMelod(self, titluri, autori, numar):
        """Genereaza si adauga melodii in fisier

        Args:
            titluri (list): lista de titluri pentru melodii
            autori (list): lista de autori pentru melodii
            numar (int): numarul de melodii de generat

        Returns:
            int: numarul de melodii diferite adaugate in fisier
        """
        to_be_added = self.__generator.generator_melodie(titluri, autori, numar)
        
        counter = 0
        for ent in to_be_added:
            try:
                self.__repo.uploadOneElem(ent)
                counter+=1
            except ValueError:
                pass
        
        return counter
        
    def exportMelodii(self, file_to_export):
        
        ent_lst = self.getAll()
        ent_lst = sorted(ent_lst, key = key_sort)
        
        with open(file_to_export, 'w') as f:
            for ent in ent_lst:
                f.write(str(ent))
        
    
        
        