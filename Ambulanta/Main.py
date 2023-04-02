from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PretragaPacijenata import PretragaPacijenata
from PregledSvihPacijenata import PregledSvihPacijenata
from RegistracijaPacijenata import RegistracijaPacijenata

class Main(QMainWindow):
    def __init__(self,pacijent):
        super().__init__()

        uic.loadUi("Main.ui",self)

        self.pacijentGumb.clicked.connect(self.pregledPacijenata)
        self.upisGumb.clicked.connect(self.upisNovihPacijenata)
        self.pregledGumb.clicked.connect(self.pregledSvihPacijenata)
        self.izlazGumb.clicked.connect(self.izlaz)

    def pregledPacijenata(self):
        self.prozorZaPretragu = PretragaPacijenata("BazaPacijenata2.db")
        self.prozorZaPretragu.show()

    def upisNovihPacijenata(self):
        self.prozorZaPretragu = RegistracijaPacijenata(self)
        self.prozorZaPretragu.show()

    def pregledSvihPacijenata(self):
        self.prozorZaPretragu = PregledSvihPacijenata(self)
        self.prozorZaPretragu.show()

    def izlaz(self):
        self.close()
