from random import randint
from entities.melodie import melodie

class generator:
    
    genuri = ["Rock","Pop","Jazz","Altele"]
    
    def generator_melodie(self, titluri:list, autori:list, numar:int):
        res = []
        for i in range(numar):
            
            titlu = titluri[randint(0, len(titluri)-1)]
            artist = autori[randint(0, len(autori)-1)]
            gen = self.genuri[randint(0, len(self.genuri)-1)]
            data = "{}/{}/{}".format(randint(1,31), randint(1,12), randint(1,2050))
            
            res.append(melodie(titlu, artist, gen, data))

        return res
    

        