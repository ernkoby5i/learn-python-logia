# https://codeshare.io/XLqXJz
# w15.04.2025 r.
#
# Praca domowa - zrobić zadanie Ile liczb
#
#
# Zadania z drugich etapów Logii
#
# Pole robota - https://logia.oeiizk.waw.pl/logia/page.php?sr=logia14/2etap
#
# > Zrobione: 6 <
#
#
    # Redukcja - https://logia.oeiizk.waw.pl/logia/page.php?sr=logia15/2etap LOGIA 15 II ETAP

# > Zrobione: 0 <

# rozw
def redukcja(n):
    n = str(n)
    czy_zmiana = False

    while True: # uwaga - to nie będzie działało z forem
        i = len(n)-1
        while i > 0:
            if n[i] == n[i-1]:
                zredukowana = str(int(n[i]) + int(n[i-1]))[-1]
                n = n[:i-1] + zredukowana + n[(i+1):]
                czy_zmiana = True
                i -= 1
            i -= 1

        if czy_zmiana == False:
            break
        else:
            czy_zmiana = False

    return int(n)


Ile liczb - https://logia.oeiizk.waw.pl/logia/page.php?sr=logia15/2etap

> Zrobione: 1 <




























































