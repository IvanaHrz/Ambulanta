class Pacijent:
    def __init__(self,ime:str,prezime:str,adresa:str,datum_rodjenja:str,oib:str,mbo:str,pov_bolesti="",terapija="",anamneza="",dijagnoza="",kir_zahvat="",lijecnik=""):
        if len(oib)!=11:
            raise Exception("OIB MORA IMATI 11 ZNAMENKI!!")
        if len(mbo)!=9:
            raise Exception("MBO MORA IMATI 9 ZNAMENKI!!")
        try:
            self.__oib = oib
        except:
            raise Exception("OIB SE SASTOJI SAMO OD ZNAMENKI!!")
        try:
            self.__mbo = mbo
        except:
            raise Exception("MBO SE SASTOJI SAMO OD ZNAMENKI!!")
        self.ime = ime
        self.prezime = prezime
        self.adresa = adresa
        self.datum_rodjenja = datum_rodjenja
        self.pov_bolesti = pov_bolesti
        self.terapija = terapija
        self.anamneza = anamneza
        self.dijagnoza = dijagnoza
        self.kir_zahvat = kir_zahvat
        self.lijecnik = lijecnik
        
    def getOib(self):
        return self.__oib
    
    def getMbo(self):
        return self.__mbo

    def setOib(self,oib):
        if len(oib)!=11:
            raise("OIB MORA IMATI 11 ZNAMENKI!!")
        try:
            self.__oib = int(oib)
        except:
            raise("OIB SE SASTOJI SAMO OD ZNAMENKI!!")

    def setMbo(self,mbo):
        if len(mbo)!=9:
            raise("MBO MORA IMATI 9 ZNAMENKI!!")
        try:
            self.__mbo = int(mbo)
        except:
            raise("MBO SE SASTOJI SAMO OD ZNAMENKI!!")

    def __str__(self) -> str:
        return self.__mbo+" "+self.ime+" "+self.prezime+" "+self.__oib+" "+self.adresa+" "+self.datum_rodjenja+" "+self.pov_bolesti+" "+self.terapija+" "+self.anamneza+" "+self.dijagnoza+" "+self.kirurski_zahvat+" "+self.lijecnik