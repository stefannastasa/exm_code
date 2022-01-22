from unittest import TestCase
from entities.melodie import melodie

from repository.melodii_repo import melodii_repo
import os

class repoTests(TestCase):
    def setUp(self):
        self.__repo = melodii_repo(filepath = 'test')
        ent_lst = []
        ent_lst.append(melodie("These things happen","G-Eazy","Altele", "01/12/2017"))
        ent_lst.append(melodie("44 Bars","Logic","Altele", "01/03/2017"))
        ent_lst.append(melodie("These things happen too","G-Eazy","Altele", "01/12/2021"))
        self.__repo.uploadList(ent_lst)
        
    def tearDown(self):
        os.remove('test')
        
    def test_load_write(self):
        ent_lst = self.__repo.getAll()
        
        self.assertEqual(len(ent_lst), 3 )