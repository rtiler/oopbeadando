from szobak import egyagyas, ketagyas
from hotel import Teszt_Hotel
from foglalas import FoglalasokB
from datetime import datetime, timedelta

# különböző dátumformátumok kezelése
def datum_tipus(datum_str):
    datum_formak = ["%Y-%m-%d", "%d-%m-%Y", "%m-%d-%Y", "%m/%d/%Y", "%d/%m/%Y", "%Y/%m/%d", "%Y.%m.%d.", "%m.%d.%Y.", "%d.%m.%Y."]
    for datum_formak in datum_formak:
        try:
            return datetime.strptime(datum_str, datum_formak)
        except ValueError:
            continue
    raise ValueError(f"{datum_str} hibás dátum.") # ha ennyi lehetőség se lenne elég akkor le kell cserélni más dátumkezelőre

# a futtatáshoz szükséges teszt hotel létrehozása
def main():
    hotel = Teszt_Hotel("Grand Budapest Hotel")
    egy_agyas = egyagyas()
    ket_agyas = ketagyas()
    hotel.add_szoba(egy_agyas)
    hotel.add_szoba(ket_agyas)

# a foglalás kezelő felület létrehozása
    foglalas_kezelo = FoglalasokB()

    while True:
        print("\n--- Foglalás kezelés ---")
        print("1. Szoba foglalás")
        print("2. Foglalás törlése")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        opcio = input("Válasszon a menüpontok közül: ")

        if opcio == "1":
            szoba_tipus = input("Adja meg a szoba típusát (1-es az egyágyas szobákhoz, 2-es a kétágyas szobákhoz): ")
            datum_str = input("Adja meg a foglalás kezdetének dátumát: ")
            ejszakak = int(input("Adja meg az eltölteni kívánt éjszakák számát: "))
            try:
                datum = datum_tipus(datum_str)
                if szoba_tipus == "1":
                    ar = foglalas_kezelo.szoba_foglalas(egy_agyas, datum, ejszakak)
                elif szoba_tipus == "2":
                    ar = foglalas_kezelo.szoba_foglalas(ket_agyas, datum, ejszakak)
                else:
                    print("Hibás szobatípus.")
                    continue
                print(f"Sikeres foglalás. Teljes ár: {ar}Ft")
            except ValueError as e:
                print(f"Hiba: {e}")

        elif opcio == "2":
            # For simplicity, let's just delete the last reservation
            if foglalas_kezelo.jelenlegi_foglalasok():
                legutobbi_foglalas = foglalas_kezelo.jelenlegi_foglalasok()[-1]
                foglalas_kezelo.foglalas_torles(legutobbi_foglalas)
                print("Legutóbbi foglalás törölve.")
            else:
                print("Nincs törölhető foglalás.")

        elif opcio == "3":
            Foglalasok = foglalas_kezelo.jelenlegi_foglalasok()
            if not Foglalasok:
                print("Nincs foglalás.")
            else:
                for idx, Foglalasok in enumerate(Foglalasok):
                    print(
                        f"{idx + 1}. Szoba típusa: {Foglalasok.szoba.szoba_tipus()}, Foglalás kezdete: {Foglalasok.datum.strftime('%Y-%m-%d')}, Éjszakák: {Foglalasok.ejszakak}, Foglalás ára: {Foglalasok.teljes_ar()}Ft")

        elif opcio == "4":
            print("Kilépés...")
            break

        else:
            print("Nincs ilyen opció, próbálja újra.")


if __name__ == "__main__":
    main()