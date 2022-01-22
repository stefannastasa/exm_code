from unittest import TestCase
from entities.melodie import melodie

from service.melodii_service import melodii_service
import os

class serviceTests(TestCase):
    def setUp(self):
        self.__serv = melodii_service(testing=True)
        ent_lst = []
        ent_lst.append(melodie("These things happen","G-Eazy","Altele", "01/12/2017"))
        ent_lst.append(melodie("44 Bars","Logic","Altele", "01/03/2017"))
        ent_lst.append(melodie("These things happen too","G-Eazy","Altele", "01/12/2021"))
        
        for ent in ent_lst:
            self.__serv.addMelodie(ent.getTitlu(), ent.getArtist(), ent.getGen(), ent.getData())
        
    def tearDown(self):
        os.remove('test')
        
    def test_searchElem(self):
        index = self.__serv.searchElem("These things happen","G-Eazy")
        self.assertEqual(index, 0)
        
        with self.assertRaises(ValueError):
            index = self.__serv.searchElem("asdf","J-Cole")
    
    
    def test_modifElem(self):
        self.__serv.modifElem(0, "Pop","12/12/2021")
        
        ent_lst = self.__serv.getAll()
        self.assertEqual(ent_lst[0].getGen(), "Pop")
        
    def test_getAll(self):
        self.assertEqual(len(self.__serv.getAll()), 3)
        
        
    def test_addMelodie(self):
        self.__serv.addMelodie("Alelujah","Nice dude","Jazz","25/12/2021")
        ent_lst = self.__serv.getAll()
        
        self.assertEqual(ent_lst[-1].getTitlu(), "Alelujah")
        self.assertEqual(ent_lst[-1].getArtist(), "Nice dude")
        self.assertEqual(ent_lst[-1].getGen(), "Jazz")
        
        
        with self.assertRaises(ValueError):
            self.__serv.addMelodie("","Nice dude","Jazz","25/12/2021")
    
    def test_searchElem(self):
        pos = self.__serv.searchElem("44 Bars","Logic")
        self.assertEqual(pos, 1)
        
        pos = self.__serv.searchElem("These things happen","G-Eazy")
        self.assertEqual(pos, 0)
    
    def test_modifElem(self):
        pos = self.__serv.searchElem("44 Bars","Logic")
        self.__serv.modifElem(pos, "Rock","27/12/2002")
        ent_lst = self.__serv.getAll()
        
        self.assertEqual(ent_lst[pos].getGen(),"Rock")
        self.assertEqual(ent_lst[pos].getData(),"27/12/2002")

    def test_genMelod(self):
        nr = self.__serv.genMelod(["asdf","asdf",'asdf'],["oooo","oooo","oo"], 10)
        ent_lst = self.__serv.getAll()

        self.assertEqual(len(ent_lst), 3 + nr)