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
        