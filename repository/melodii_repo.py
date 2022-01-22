from entities.melodie import melodie


class melodii_repo:
    def __init__(self, filepath = 'resources/melodii'):
        self.__file = filepath
        
    def __load__all__from__file(self):
        """Incarca toate melodiile din fisier.

        Returns:
            list: lista cu melodiile din fisier
        """
        ent_list = []
        try:
            f = open(self.__file, 'r')
            for line in f:
                line = line.split(';')
                if len(line) == 5:
                    line = line[:-1]
                    ent_list.append(melodie(*line))
                
        except OSError:
            f = open(self.__file, 'w')
        
        f.close()
        return ent_list
    
    def __write__all__to__file(self, ent_lst):
        """Scrie toate elementele din 'ent_lst' in fisier

        Args:
            ent_lst (list): lista de elemente
        """
        with open(self.__file, "w") as f:
            for ent in ent_lst:
                f.write(ent.fileFormat())
            
    
    def uploadList(self, ent_lst):
        self.__write__all__to__file(ent_lst)    
    
    def uploadOneElem(self, ent:melodie):
        """Uploads only one element to the file

        Args:
            ent (melodie): the element to be added
        """
        ent_lst = self.getAll()
        if ent not in ent_lst:
            with open(self.__file, 'a') as f:
                f.write(ent.fileFormat())
        else:
            raise ValueError("Melodie duplicat.")
    
    def getAll(self):
        return self.__load__all__from__file()
    
    