from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from Main import Main
import sqlite3

with sqlite3.connect("BazaPacijenata2.db") as conn:
    suceljeZaNaredbe = conn.cursor()
    #suceljeZaNaredbe.execute("DROP TABLE IF EXISTS Pacijenti;") #Zakomentirati kad više ne treba
    upit = "CREATE TABLE IF NOT EXISTS Pacijenti(MBO INTEGER PRIMARY KEY UNIQUE NOT NULL, Ime CHAR(20), Prezime CHAR(30), Adresa CHAR(50), Datum_rodjenja DATE, OIB INT(11), Pov_bolesti CHAR(200), Terapija CHAR(200), Anamneza CHAR(200), Dijagnoza CHAR(200), Kir_zahvat CHAR(200), Lijecnik CHAR(50));"
    suceljeZaNaredbe.execute(upit)

app = QApplication(sys.argv)
prozor = Main(pacijent=[])
prozor.show()
sys.exit(app.exec())