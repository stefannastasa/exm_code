from random import randint
from entities.melodie import melodie

class generator:
    
    genuri = ["Rock","Pop","Jazz","Altele"]
    
    def generator_melodie(self, titluri:list, autori:list, numar:int):
        """Functie care genereaza melodii dupa listele date

        Args:
            titluri (list): lista de titluri pentru melodiile generate
            autori (list): lista de autori pentru melodiile generate
            numar (int): numarul total de melodii generate

        Returns:
            list: lista de melodii generate
        """
        res = []
        for i in range(numar):
            
            titlu = titluri[randint(0, len(titluri)-1)]
            artist = autori[randint(0, len(autori)-1)]
            gen = self.genuri[randint(0, len(self.genuri)-1)]
            data = "{}/{}/{}".format(randint(1,28), randint(1,12), randint(1,2050))
            
            res.append(melodie(titlu, artist, gen, data))

        return res
    

        