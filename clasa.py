def poler(droga):
    szerokosc = 0
    wysokosc = 0
    min_szerokosc = 0
    max_szerokosc = 0
    min_wysokosc = 0
    max_wysokosc = 0

    for ruch in trasa:
        if ruch == 'g':
            wysokosc = wysokosc + 1
        elif ruch == 'd':
            wysokosc = wysokosc - 1
        elif ruch == 'p':
            szerokosc = szerokosc + 1
        elif ruch == 'l':
            szerokosc = szerokosc - 1

        min_szerokosc = min(min_szerokosc, szerokosc)
        max_szerokosc = max(max_szerokosc, szerokosc)
        min_wysokosc = min(min_wysokosc, wysokosc)
        max_wysokosc = max(max_wysokosc, wysokosc)

    szerokosc_KONIEC = max_szerokosc - min_szerokosc
    wysokosc_KONIEC = max_wysokosc - min_wysokosc

    return szerokosc_KONIEC * wysokosc_KONIEC


trasa = "gpgpld"
print(poler(trasa))





