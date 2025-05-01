# Drugie - Ślimak https://logia.oeiizk.waw.pl/logia/page.php?sr=logia13/2etap


def kiedy(rano,noc,spadek):
    jestem_na = 0
    c = 0
    dzien = 0
    while True:
        c = c+1
        if c%2!=0:
            jestem_na = jestem_na + rano
            dzien = dzien + 1
        else:
            jestem_na = jestem_na + noc
            jestem_na= jestem_na - spadek

        if  jestem_na>=1000:
            return dzien

        najblizsza_polka = (jestem_na // spadek) * spadek

        if jestem_na < najblizsza_polka:
            jestem_na = najblizsza_polka


print(kiedy(5, 3, 2))


