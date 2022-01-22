from datetime import date

class validator:

    def validateGen(self,gen):
        if gen.lower() not in ["rock","pop","jazz","altele"]:
            raise ValueError("Genul trebuie sa fie una dintre: 'Rock','Pop','Jazz','Altele'")
        
    def validateData(self, data):
        try:
            data = data.split('/')
            data = date(int(data[2]), int(data[1]), int(data[0]))
        except :
            raise ValueError("Data este invalida.")
        
        
    def validate(self, gen, data):
        if gen.lower() not in ["rock","pop","jazz","altele"]:
            raise ValueError("Genul trebuie sa fie una dintre: 'Rock','Pop','Jazz','Altele'")
        
        try:
            data = data.split('/')
            data = date(int(data[2]), int(data[1]), int(data[0]))
        except :
            raise ValueError("Data este invalida.")