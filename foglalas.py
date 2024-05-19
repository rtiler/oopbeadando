from datetime import datetime #dátumkezeléshez szükséges import
# normál osztály a foglalások kezeléséhez
class FoglalasokA:
    def __init__(self, szoba, datum, ejszakak):
        self.szoba = szoba
        self.datum = datum
        self.ejszakak = ejszakak
# adott szoba árának a kiszámítása
    def teljes_ar(self):
        return self.szoba.arpereste * self.ejszakak
# a megadott dátum ellenőrzése után a metódus elmenti a foglalást
class FoglalasokB:
    def __init__(self):
        self.FoglalasokB = []

    def szoba_foglalas(self, szoba, datum, ejszakak):
        if datum <= datetime.now():
            raise ValueError("Szobát foglalni csakis jövőbeli dátumra lehet")
        Foglalas = FoglalasokA(szoba, datum, ejszakak)
        self.FoglalasokB.append(Foglalas)
        return Foglalas.teljes_ar()
# a legfrissebben megadott (legutóbbi) foglalást törli a listából
    def foglalas_torles(self, Foglalas):
        self.FoglalasokB.remove(Foglalas)
# kiírja a foglalások listáját
    def jelenlegi_foglalasok(self):
        return self.FoglalasokB