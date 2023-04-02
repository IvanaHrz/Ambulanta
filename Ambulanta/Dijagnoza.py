from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Pacijent import Pacijent # ne može pronaci Pacijent
import sqlite3


class Dijagnoza(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Dijagnoza.ui",self)

        self.dijagnoze = []
        with sqlite3.connect("BazaPacijenata2.db") as conn:
            suceljeZaNaredbe = conn.cursor()
            upit = "SELECT Pov_bolesti, Terapija, Anamneza, Dijagnoza, Kir_zahvat, Lijecnik FROM Pacijenti WHERE Pacijenti.MBO="+self.mboText.text()+";"
            rezultat = suceljeZaNaredbe.execute(upit)
            for ntorka in rezultat:
                novaDijagnoza = Dijagnoza(pov_bolesti = ntorka[0],terapija = ntorka[1],anamneza = ntorka[2],dijagnoza = ntorka[3],kirurski_zahvat = ntorka[4],lijecnik = ntorka[5])
                self.dijagnoze.append(novaDijagnoza)
        
        self.unesiGumb.clicked.connect(self.unosDijagnoze)
        self.natragGumb.clicked.connect(self.zatvoriMe)
        
    def __porukaProzor(self,poruka):
        porukaProzor = QMessageBox()
        porukaProzor.setIcon(QMessageBox.Warning)
        porukaProzor.setText(poruka)
        porukaProzor.setStandardButtons(QMessageBox.Ok)
        porukaProzor.exec()

    def unosDijagnoze(self):
        nova_dijagnoza = Dijagnoza(pov_bolesti=self.pov_bolestiText.text(),terapija=self.terapijaText.text(),anamneza=self.anamnezaText.text(),dijagnoza=self.dijagnozaText.text(),kirurski_zahvat=self.kirurski_zahvatText.text(),lijecnik=self.lijecnikText.text())
        with sqlite3.connect("BazaPacijenata2.db") as conn:
            suceljeZaNaredbe = conn.cursor()
            upit = f"INSERT INTO Pacijenti(Pov_bolesti,Terapija,Anamneza,Dijagnoza,Kir_zahvat,Lijecnik) VALUES('{nova_dijagnoza.pov_bolesti}','{nova_dijagnoza.terapija}','{nova_dijagnoza.anamneza}','{nova_dijagnoza.dijagnoza}','{nova_dijagnoza.kirurski_zahvat}','{nova_dijagnoza.lijecnik}')"
            suceljeZaNaredbe.execute(upit)
        self.dijagnoze.append(nova_dijagnoza)
        self.__porukaProzor("Dijagnoza uspješno unesena!!","information")
        
    def obrisi(self):
        self.pov_bolestiText.setText("")
        self.terapijaText.setText("")
        self.anamnezaText.setText("")
        self.dijagnozaText.setText("")
        self.kirurski_zahvatText.setText("")
        self.lijecnikText.setText("")
        
    def zatvoriMe(self):
        self.close()
