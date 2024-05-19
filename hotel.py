from abc import ABC, abstractmethod
#hotel absztrakt osztály
class Hotel(ABC):
    def __init__(self, nev):
        self.nev = nev
        self.szobak1 = []
#hotel feltöltése szobákkal
    def add_szoba(self, szoba):
        self.szobak1.append(szoba)

    @abstractmethod
    def hotel_nev(self):
        pass
#származtatott osztály hogy egy adott hotellel dolgozzon majd a program
class Teszt_Hotel(Hotel):
    def __init__(self, nev):
        super().__init__(nev)

    def hotel_nev(self):
        return self.nev