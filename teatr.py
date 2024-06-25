#Teatr - zarządzanie miejscami, ćwiczenia 50 SŁOŃ i LEW
class MiejsceTeatralne:
    def __init__(self, numer, cena):
        self.numer = numer
        self.cena = cena
        self.dostepne = True

#Miejsca teatralne - poprawić udogodnienia !!!!!!!!!
class MiejsceZwykle(MiejsceTeatralne):
    def __init__(self, numer):
        super().__init__(numer, cena=50)

class MiejsceVIP(MiejsceTeatralne):
    def __init__(self, numer):
        super().__init__(numer, cena=100)
        self.udogodnienia = "szerokie fotele"

class MiejsceDlaNiepelnosprawnych(MiejsceTeatralne):
    def __init__(self, numer):
        super().__init__(numer, cena=25)
        self.udogodnienia = "wejście na słuchawki"

class Teatr: #10 miejsc, 6 zwyklych, 2 vip, 2 niepelnosprawne -> cwiczenie LISTY SKŁADANE
    def __init__(self):
        self.miejsca = [MiejsceZwykle(i + 1) for i in range(6)] + [MiejsceVIP(i + 7) for i in range(2)] + [MiejsceDlaNiepelnosprawnych(i + 9) for i in range(2)]

    def pokaz_miejsca(self):
        for miejsce in self.miejsca:
            status = 'Wolne' if miejsce.dostepne else 'Zarezerwowane'
            udogodnienia = getattr(miejsce, 'udogodnienia', '')
            if udogodnienia:
                print(f'Miejsce {miejsce.numer} ({type(miejsce).__name__}): {status}, Cena: {miejsce.cena} PLN, Udogodnienia: {udogodnienia}')
            else:
                print(f'Miejsce {miejsce.numer} ({type(miejsce).__name__}): {status}, Cena: {miejsce.cena} PLN')


    def rezerwuj_miejsce(self, numer):
        if 1 <= numer <= len(self.miejsca):
            miejsce = self.miejsca[numer - 1]
            if miejsce.dostepne:
                miejsce.dostepne = False
                print(f'Miejsce {miejsce.numer} zostało zarezerwowane')
            else:
                print(f'Miejsce {miejsce.numer} jest już zarezerwowane')
        else:
            print('Nieprawidłowy numer miejsca.')

    def anuluj_rezerwacje(self, numer): ##############IF NOT z ćwiczenia 42 - funkcja z parametrami
        if 1 <= numer <= len(self.miejsca):
            miejsce = self.miejsca[numer - 1]
            if not miejsce.dostepne:
                miejsce.dostepne = True
                print(f'Rezerwacja miejsca {miejsce.numer} została anulowana')
            else:
                print(f'Miejsce {miejsce.numer} nie jest objęte rezerwacją')
        else:
            print('Nieprawidłowy numer miejsca.')


class Klient:
    def __init__(self, id_klienta, imie, nazwisko):
        self.id_klienta = id_klienta
        self.imie = imie
        self.nazwisko = nazwisko


def main():
    teatr = Teatr()

    while True:
        while True:
            imie = input('Podaj swoje imię: ')
            if imie.isalpha():
                break
            else:
                print("BŁĄD! Wpisz poprawne imię, które składa się TYLKO z liter.")

        while True:
            nazwisko = input('Podaj swoje nazwisko: ')
            if nazwisko.isalpha():
                break
            else:
                print("BŁĄD! Wpisz poprawne nazwisko, które składa się TYLKO z liter.")

        klient = Klient(1, imie, nazwisko) #Klient permanentnie ma nowy ID, nowy klient nadpisuje poprzednie zamówienie FIX!

        while True:
            print(f'\nWitaj {klient.imie} {klient.nazwisko}! Oto dostępne miejsca:')
            teatr.pokaz_miejsca()

            print("\nOpcje:")
            print("1. Rezerwuj miejsce")
            print("2. Anuluj rezerwację")
            print("3. Powrót do ekranu głównego")
            wybor = input("Wybierz opcję (1-3) lub wpisz 'exit' aby zakończyć: ")

            if wybor == '1':
                numer_miejsca = int(input('Podaj numer miejsca do rezerwacji: '))
                teatr.rezerwuj_miejsce(numer_miejsca)
            elif wybor == '2':
                numer_miejsca = int(input('Podaj numer miejsca do anulowania rezerwacji: '))
                teatr.anuluj_rezerwacje(numer_miejsca)
            elif wybor == '3':
                break
            elif wybor.lower() == 'exit':
                return
            else:
                print('Nieprawidłowy wybór.')


if __name__ == '__main__':
    main()

