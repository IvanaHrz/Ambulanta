from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Pacijent import Pacijent # ne može pronaci Pacijent
import sqlite3

class PregledSvihPacijenata(QWidget):
    def __init__(self,pacijenti:dict):
        super().__init__()
        uic.loadUi("PregledSvihPacijenata.ui",self)

        self.pacijenti = pacijenti

        with sqlite3.connect("BazaPacijenata2.db") as conn:
            suceljeZaNaredbe = conn.cursor()
            upit = "SELECT Ime, Prezime, MBO FROM Pacijenti;"
            rezultat = suceljeZaNaredbe.execute(upit).fetchall()

            tekst = "Ime\tPrezime\tMBO\n-------------------------------------------------------------------------------------------------\n"
            for n in rezultat:
                pacijentko = n[0],n[1],n[2]
                tekst+=str(pacijentko)+"\n"
         
            self.pacijentiEdit.setReadOnly(False)
            self.pacijentiEdit.setPlainText(tekst)
            self.pacijentiEdit.setReadOnly(True)

            self.zatvoriGumb.clicked.connect(self.zatvoriMe)
        
    def zatvoriMe(self):
        self.close()