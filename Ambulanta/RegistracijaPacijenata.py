from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Pacijent import Pacijent
import sqlite3

class RegistracijaPacijenata(QWidget):
    def __init__(self,pacijent):
        super().__init__()

        uic.loadUi("RegistracijaPacijenata.ui",self)

        self.pacijent = pacijent
        self.pacijenti = []

        with sqlite3.connect("BazaPacijenata2.db") as conn:
            suceljeZaNaredbe = conn.cursor()
            upit = "SELECT Ime, Prezime, OIB, MBO, Datum_rodjenja, Adresa FROM Pacijenti;"
            rezultat = suceljeZaNaredbe.execute(upit)
            for ntorka in rezultat:
                ntorka3 = ntorka[3]
                if len(str(ntorka[3]))!=9:
                    ntorka3 = "0"*(9-len(str(ntorka[3])))+str(ntorka[3])
                noviPacijent = Pacijent(ime = ntorka[0], prezime = ntorka[1], oib = str(ntorka[2]), mbo = str(ntorka3), datum_rodjenja = ntorka[4], adresa = ntorka[5])
                self.pacijenti.append(noviPacijent)
            
        self.unosGumb.clicked.connect(self.unosPacijenta)
        self.brisiGumb.clicked.connect(self.obrisi)
        self.izlazGumb.clicked.connect(self.zatvoriMe)

    def __porukaProzor(self,poruka:str,stoJe="warning"):
        porukaProzor = QMessageBox()
        if stoJe=="warning":
            porukaProzor.setIcon(QMessageBox.Warning)
        else:
            porukaProzor.setIcon(QMessageBox.Information)
        porukaProzor.setText(poruka)
        porukaProzor.setStandardButtons(QMessageBox.Ok)

        porukaProzor.exec()

    def unosPacijenta(self):
        try:
            noviPacijent = Pacijent(ime=self.imeText.text(),prezime=self.prezimeText.text(),adresa=self.adresaText.text(),datum_rodjenja=self.datum_rodjenjaText.text(),oib=self.oibText.text(),mbo=self.mboText.text(), pov_bolesti="",terapija="",anamneza="",dijagnoza="",kirurski_zahvat="") 
            oibPostoji = False
            
            for pacijent in self.pacijenti:
                oib = pacijent.getOib()
                mbo = pacijent.getMbo()
                if oib == self.oibText.text():
                    oibPostoji = True
                    break
            
            mbo = self.mboText.text()
            
            if mbo in self.pacijenti:
                self.__porukaProzor("POGREŠKA! Pacijent s tim MBO-om već postoji!!")
            
            if oibPostoji:
                self.__porukaProzor("POGREŠKA! Pacijent s tim OIB-om već postoji!!")

            else:
                try:
                    with sqlite3.connect("BazaPacijenata2.db") as conn:
                        suceljeZaNaredbe = conn.cursor()
                        upit = f"INSERT INTO Pacijenti(Ime, Prezime, OIB, MBO, Datum_rodjenja, Adresa) VALUES('{noviPacijent.ime}','{noviPacijent.prezime}','{noviPacijent.getOib()}','{noviPacijent.getMbo()}','{noviPacijent.datum_rodjenja}','{noviPacijent.adresa}');"
                        print(upit)
                        suceljeZaNaredbe.execute(upit)
                    self.pacijenti.append(noviPacijent)
                    self.__porukaProzor(f"Pacijent {noviPacijent.ime} {noviPacijent.prezime} uspješno unesen!!","information")

                except Exception as exc:
                    self.__porukaProzor(str(exc))
        except Exception as exc:
            self.__porukaProzor(str(exc))

        
    def obrisi(self):
        self.imeText.setText("")
        self.prezimeText.setText("")
        self.oibText.setText("")
        self.mboText.setText("")
        self.datum_rodjenjaText.setText("")
        self.adresaText.setText("")
        
    def zatvoriMe(self):
        self.close()
