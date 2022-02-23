import sys

stan_konta  = 0
historia_akcji = []
historia_wyborow = []
stan_magazynowy_zakupionego_towaru = dict()
zmiana_na_koncie_gr = 0
akcje=["saldo", "zakup", "sprzedaz", "konto", "magazyn", "przegląd", "stop"]
print("Jaką akcję chcesz wykonać?")

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
        zmiana_na_koncie_gr = int(input())
        print("Dodaj komentarz do zmian")
        komentarz_do_zmiany = input()
        stan_konta += zmiana_na_koncie_gr
        historia_akcji.append([rodzaj_akcji,zmiana_na_koncie_gr, komentarz_do_zmiany])
    if rodzaj_akcji == "zakup":
        historia_wyborow.append(rodzaj_akcji)
        identyfikator_produktu = str(input("Podaj nazwę produktu"))
        cena_jednostkowa = int(input("Podaj cenę produktu"))
        liczba_sztuk = int(input("Ile sztuk chcesz kupić?"))
        historia_akcji.append([rodzaj_akcji, identyfikator_produktu, cena_jednostkowa, liczba_sztuk])
        if stan_konta - cena_jednostkowa * liczba_sztuk < 0:
            print("Błąd za mało środków na koncie", stan_konta)
            continue
        stan_konta -= cena_jednostkowa * liczba_sztuk
        if identyfikator_produktu in stan_magazynowy_zakupionego_towaru:
            stan_magazynowy_zakupionego_towaru[identyfikator_produktu] += liczba_sztuk
        else:
            stan_magazynowy_zakupionego_towaru[identyfikator_produktu] = liczba_sztuk

    if rodzaj_akcji == "sprzedaz":
        historia_wyborow.append(rodzaj_akcji)
        identyfikator_produktu = str(input("Podaj nazwę produktu"))
        cena_jednostkowa = int(input("Podaj cenę produktu"))
        liczba_sztuk = int(input("Ile sztuk chcesz sprzedać?"))
        historia_akcji.append([rodzaj_akcji, identyfikator_produktu, cena_jednostkowa, liczba_sztuk])
        if stan_magazynowy_zakupionego_towaru[identyfikator_produktu] < liczba_sztuk:
            print("Błąd za mało sztuk w magazynie", liczba_sztuk, stan_magazynowy_zakupionego_towaru)
            continue
        if identyfikator_produktu not in stan_magazynowy_zakupionego_towaru:
            print("Błąd brak produktu w magazynie", identyfikator_produktu)
            continue
        if stan_magazynowy_zakupionego_towaru[identyfikator_produktu] >= liczba_sztuk:
            stan_magazynowy_zakupionego_towaru[identyfikator_produktu] -= liczba_sztuk
            stan_konta += cena_jednostkowa * liczba_sztuk

    if rodzaj_akcji == "konto":
        print(stan_konta)
        break
    if rodzaj_akcji == "magazyn":

        while True:
            identyfikator_produktu = str(input("Podaj nazwę produktu"))
            if identyfikator_produktu == "":
                break

            print(f"{identyfikator_produktu}: {stan_magazynowy_zakupionego_towaru[identyfikator_produktu]}")
    if rodzaj_akcji == "Przegląd":

        h=1
        while h < len(historia_akcji):
            print(f"{h+1}: {historia_akcji[h]}")
            h += 1
        del h

    if rodzaj_akcji != "stop":
        continue

    if len(sys.argv) >= 2:
        rodzaj_akcji = sys.argv[1]

    if rodzaj_akcji not in akcje:
        print("Błąd nierozpoznana akcja ", rodzaj_akcji)
        break


    if rodzaj_akcji == "saldo":
        historia_wyborow.append(rodzaj_akcji)
        zmiana_na_koncie_gr = int(sys.argv[2])
        print("Dodaj komentarz do zmian")
        komentarz_do_zmiany = sys.argv[3]
        stan_konta += zmiana_na_koncie_gr
        historia_akcji.append([rodzaj_akcji,zmiana_na_koncie_gr, komentarz_do_zmiany])
        for rzad in historia_akcji:
            for element in rzad:
                print(element)
        print("stop")


    if rodzaj_akcji == "zakup":
        historia_wyborow.append(rodzaj_akcji)
        identyfikator_produktu = str(sys.argv[2])
        cena_jednostkowa = int(sys.argv[3])
        liczba_sztuk = int(sys.argv[4])
        historia_akcji.append([rodzaj_akcji, identyfikator_produktu, cena_jednostkowa, liczba_sztuk])
        if stan_konta - cena_jednostkowa * liczba_sztuk < 0:
            print("Błąd za mało środków na koncie", stan_konta)
            continue
        stan_konta -= cena_jednostkowa * liczba_sztuk
        if identyfikator_produktu in stan_magazynowy_zakupionego_towaru:
            stan_magazynowy_zakupionego_towaru[identyfikator_produktu] += liczba_sztuk
        else:
            stan_magazynowy_zakupionego_towaru[identyfikator_produktu] = liczba_sztuk
        for rzad in historia_akcji:
            for element in rzad:
                print(element)
        print("stop")

    if rodzaj_akcji == "sprzedaz":

        historia_wyborow.append(rodzaj_akcji)
        identyfikator_produktu = str(sys.argv[2])
        cena_jednostkowa = int(sys.argv[3])
        liczba_sztuk = int(sys.argv[4])
        historia_akcji.append([rodzaj_akcji, identyfikator_produktu, cena_jednostkowa, liczba_sztuk])
        if stan_magazynowy_zakupionego_towaru[identyfikator_produktu] < liczba_sztuk:
            print("Błąd za mało sztuk w magazynie", liczba_sztuk, stan_magazynowy_zakupionego_towaru)
            continue
        if identyfikator_produktu not in stan_magazynowy_zakupionego_towaru:
            print("Błąd brak produktu w magazynie", identyfikator_produktu)
            continue
        if stan_magazynowy_zakupionego_towaru[identyfikator_produktu] >= liczba_sztuk:
            stan_magazynowy_zakupionego_towaru[identyfikator_produktu] -= liczba_sztuk
            stan_konta += cena_jednostkowa * liczba_sztuk
        for rzad in historia_akcji:
            for element in rzad:
                print(element)
        print("stop")

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

        print(sys.argv[2:])
        for identyfikator_produktu in sys.argv[2:]:

            if identyfikator_produktu in stan_magazynowy_zakupionego_towaru:
                print(f"{identyfikator_produktu}: {stan_magazynowy_zakupionego_towaru[identyfikator_produktu]}" )
            else:
                print(f"{identyfikator_produktu}: 0" )



    if rodzaj_akcji == "przegląd":
        print("przeglad")
        przeglad_od = int(sys.argv[2])
        przeglad_do = int(sys.argv[3])
        print(historia_akcji[przeglad_od:przeglad_do + 1])
        for instrukcja in historia_akcji[przeglad_od:przeglad_do+1]:

            for linia in instrukcja:
                print(linia)
        print("stop")

    break
