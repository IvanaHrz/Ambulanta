from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Pacijent import Pacijent  # ne može pronaci Pacijent
import sqlite3


class PretragaPacijenata(QWidget):
    def __init__(self,pacijenti):
        super().__init__()
        uic.loadUi("PretragaPacijenata.ui",self)

        self.pacijenti = pacijenti

        self.pretragaGumb.clicked.connect(self.pretrazi)
        self.obrisiGumb.clicked.connect(self.obrisi)
        self.dijagnozaGumb.clicked.connect(self.pretrazidijagnozu)
        self.natragGumb.clicked.connect(self.zatvoriMe)
    
    def __porukaProzor(self,poruka):
        porukaProzor = QMessageBox()
        porukaProzor.setIcon(QMessageBox.Warning)
        porukaProzor.setText(poruka)
        porukaProzor.setStandardButtons(QMessageBox.Ok)
        porukaProzor.exec()

    def __otkljucaj(self):
        self.imeText.setReadOnly(False)
        self.prezimeText.setReadOnly(False)
        self.oibText.setReadOnly(False)
        self.datumRodjenjaText.setReadOnly(False)
        self.adresaText.setReadOnly(False)
        
    def __zakljucaj(self):
        self.imeText.setReadOnly(True)
        self.prezimeText.setReadOnly(True)
        self.oibText.setReadOnly(True)
        self.datumRodjenjaText.setReadOnly(True)
        self.adresaText.setReadOnly(True)
        
    def pretrazi(self):
        try:
            rez = None
            with sqlite3.connect("BazaPacijenata2.db") as conn:
                suceljeZaNaredbe = conn.cursor()
                upit="SELECT Ime, Prezime, OIB, MBO,Datum_rodjenja, Adresa FROM Pacijenti WHERE Pacijenti.MBO="+self.mboText.text()+";"
                rez = suceljeZaNaredbe.execute(upit).fetchall()
            if rez is None or len(rez)==0:
                self.__porukaProzor("Pacijent s tim MBO-om NE POSTOJI!!")
            else:
                self.__otkljucaj()
                pacijentko = rez[0]
                self.imeText.setText(pacijentko[0])
                self.prezimeText.setText(pacijentko[1])
                self.oibText.setText(str(pacijentko[2]))
                self.datumRodjenjaText.setText(pacijentko[4])
                self.adresaText.setText(pacijentko[5])
                self.__zakljucaj()
        except:
            self.__porukaProzor("POGREŠAN UNOS ZA MBO!!")

    
    def obrisi(self):
        self.mboText.setText("")
        
               
    def pretrazidijagnozu(self):
        self.prozorZaPretragu = Pacijent("BazaPacijenata2.db")
        self.prozorZaPretragu.show()


    def zatvoriMe(self):
        self.close()
