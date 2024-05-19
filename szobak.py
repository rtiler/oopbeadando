from abc import ABC, abstractmethod
from datetime import datetime, timedelta
# absztrakt osztály a szobák létrehozásához
class Szoba(ABC):
    def __init__(self, arpereste):
        self.arpereste = arpereste

    @abstractmethod
    def szoba_tipus(self):
        pass
# a két lehetséges szoba típus az áraikkal
class egyagyas(Szoba):
    def __init__(self):
        super().__init__(arpereste=30000)

    def szoba_tipus(self):
        return "Egy ágyas szoba"

class ketagyas(Szoba):
    def __init__(self):
        super().__init__(arpereste=50000)

    def szoba_tipus(self):
        return "Két ágyas szoba"