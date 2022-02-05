import sys

stan_konta  = 0
historia_akcji = []
historia_wyborow = []
stan_magazynowy_zakupionego_towaru = dict()
zmiana_na_koncie_gr = 0
#liczba_sztuk = 0
#cena_jednostkowa = 0
#identyfiktor_produktu = ""
akcje=["saldo", "zakup", "sprzedaz", "konto", "magazyn", "przegląd", "stop"]
print("Jaką akcję chcesz wykonać?")

#rodzaj_akcji=str(sys.argv[1])
#identyfiktor_produktu=str(sys.argv[2])
#cena_jednostkowa=int(sys.argv[3])
#liczba_sztuk=int(sys.argv[4])

identyfiktor_produktu = ""
cena_jednostkowa = 0
liczba_sztuk = 0

while True:
    rodzaj_akcji = str(input())
    if rodzaj_akcji not in akcje:
        print("Błąd nierozpoznana akcja ", rodzaj_akcji)
        break
    if rodzaj_akcji == "saldo":
        historia_wyborow.append(rodzaj_akcji)
        historia_akcji.append(rodzaj_akcji)
        zmiana_na_koncie_gr = int(input())
        historia_akcji.append(zmiana_na_koncie_gr)
        print("Dodaj komentarz do zmian")
        komentarz_do_zmiany = input()
        historia_akcji.append(komentarz_do_zmiany)
        stan_konta += zmiana_na_koncie_gr
    if rodzaj_akcji == "zakup":
        historia_akcji.append(rodzaj_akcji)
        historia_wyborow.append(rodzaj_akcji)
        identyfikator_produktu = str(input("Podaj nazwę produktu"))
        historia_akcji.append(identyfikator_produktu)
        cena_jednostkowa = int(input("Podaj cenę produktu"))
        historia_akcji.append(cena_jednostkowa)
        liczba_sztuk = int(input("Ile sztuk chcesz kupić?"))
        historia_akcji.append(liczba_sztuk)
        if stan_konta - cena_jednostkowa * liczba_sztuk < 0:
            print("Błąd za mało środków na koncie", stan_konta)
            continue
        stan_konta -= cena_jednostkowa * liczba_sztuk
        if identyfikator_produktu in stan_magazynowy_zakupionego_towaru:
            stan_magazynowy_zakupionego_towaru[identyfikator_produktu] += liczba_sztuk
        else:
            stan_magazynowy_zakupionego_towaru[identyfikator_produktu] = liczba_sztuk
    if rodzaj_akcji == "sprzedaz":
        historia_akcji.append(rodzaj_akcji)
        historia_wyborow.append(rodzaj_akcji)
        identyfikator_produktu = str(input("Podaj nazwę produktu"))
        historia_akcji.append(identyfikator_produktu)
        cena_jednostkowa = int(input("Podaj cenę produktu"))
        historia_akcji.append(cena_jednostkowa)
        liczba_sztuk = int(input("Ile sztuk chcesz sprzedać?"))
        historia_akcji.append(liczba_sztuk)
        if stan_magazynowy_zakupionego_towaru[identyfikator_produktu] < liczba_sztuk:
            print("Błąd za mało sztuk w magazynie", liczba_sztuk, stan_magazynowy_zakupionego_towaru)
            continue
        if identyfikator_produktu not in stan_magazynowy_zakupionego_towaru:
            print("Błąd brak produktu w magazynie", identyfikator_produktu)
            continue
        if stan_magazynowy_zakupionego_towaru[identyfikator_produktu] >= liczba_sztuk:
            stan_magazynowy_zakupionego_towaru[identyfikator_produktu] -= liczba_sztuk
            stan_konta += cena_jednostkowa * liczba_sztuk
    if rodzaj_akcji == "stop":
        historia_akcji.append(rodzaj_akcji)
        print(stan_konta)
        print(historia_akcji)
        print(historia_wyborow)
        break
    if rodzaj_akcji == "konto":
        historia_akcji.append(rodzaj_akcji)
        print(stan_konta)
        break
    if rodzaj_akcji == "magazyn":
        historia_akcji.append(rodzaj_akcji)
        while True:
            identyfikator_produktu = str(input("Podaj nazwę produktu"))
            if identyfikator_produktu == "":
                break
            historia_akcji.append(identyfikator_produktu)
            print(f"{identyfikator_produktu}: {stan_magazynowy_zakupionego_towaru[identyfikator_produktu]}")
    if rodzaj_akcji == "Przegląd":
        historia_akcji.append(rodzaj_akcji)
        h=1
        while h < len(historia_akcji):
            print(f"{h+1}: {historia_akcji[h]}")
            h += 1
        del h

    if len(sys.argv) == 2:
        rodzaj_akcji = sys.argv[1]
    if rodzaj_akcji not in akcje:
        print("Błąd nierozpoznana akcja ", rodzaj_akcji)
        break
    if rodzaj_akcji == "zakup":
        historia_akcji.append(rodzaj_akcji)
        historia_wyborow.append(rodzaj_akcji)
        identyfikator_produktu = str(sys.argv[2])
        historia_akcji.append(identyfikator_produktu)
        cena_jednostkowa = int(sys.argv[3])
        historia_akcji.append(cena_jednostkowa)
        liczba_sztuk = int(sys.argv[4])
        historia_akcji.append(liczba_sztuk)
        if stan_konta - cena_jednostkowa * liczba_sztuk < 0:
            print("Błąd za mało środków na koncie", stan_konta)
            continue
        stan_konta -= cena_jednostkowa * liczba_sztuk
        if identyfikator_produktu in stan_magazynowy_zakupionego_towaru:
            stan_magazynowy_zakupionego_towaru[identyfikator_produktu] += liczba_sztuk
        else:
            stan_magazynowy_zakupionego_towaru[identyfikator_produktu] = liczba_sztuk
    if rodzaj_akcji == "sprzedaz":
        historia_akcji.append(rodzaj_akcji)
        historia_wyborow.append(rodzaj_akcji)
        identyfikator_produktu = str(sys.argv[2])
        historia_akcji.append(identyfikator_produktu)
        cena_jednostkowa = int(sys.argv[3])
        historia_akcji.append(cena_jednostkowa)
        liczba_sztuk = int(sys.argv[4])
        historia_akcji.append(liczba_sztuk)
        if stan_magazynowy_zakupionego_towaru[identyfikator_produktu] < liczba_sztuk:
            print("Błąd za mało sztuk w magazynie", liczba_sztuk, stan_magazynowy_zakupionego_towaru)
            continue
        if identyfikator_produktu not in stan_magazynowy_zakupionego_towaru:
            print("Błąd brak produktu w magazynie", identyfikator_produktu)
            continue
        if stan_magazynowy_zakupionego_towaru[identyfikator_produktu] >= liczba_sztuk:
            stan_magazynowy_zakupionego_towaru[identyfikator_produktu] -= liczba_sztuk
            stan_konta += cena_jednostkowa * liczba_sztuk
    if rodzaj_akcji == "stop":
        historia_akcji.append(rodzaj_akcji)
        print(stan_konta)
        print(historia_akcji)
        print(historia_wyborow)
        break
    if rodzaj_akcji == "konto":
        historia_akcji.append(rodzaj_akcji)
        print(stan_konta)
        break
    if rodzaj_akcji == "magazyn":
        historia_akcji.append(rodzaj_akcji)
        while True:
            identyfikator_produktu = str(sys.argv[2, 3, 4])
            if identyfikator_produktu == "":
                break
            historia_akcji.append(identyfikator_produktu)
            print(f"{identyfikator_produktu}: {stan_magazynowy_zakupionego_towaru[identyfikator_produktu]}")
    if rodzaj_akcji == "Przegląd":
        historia_akcji.append(rodzaj_akcji)
        h = 1
        while h < len(historia_akcji):
            print(f"{h + 1}: {historia_akcji[h]}")
            h += 1
        del h


