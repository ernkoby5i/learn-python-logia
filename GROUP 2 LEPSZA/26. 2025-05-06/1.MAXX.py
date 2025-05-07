# zadanie Maxx - https://logia.oeiizk.waw.pl/logia/page.php?sr=logia08/2etap

def MAXX(slowo):
    n = len(slowo)
    max_len = 0
    wynik = slowo[0]

    for i in range(n):
        for j in range(n - 1, i, -1):
            if slowo[i] == slowo[j]:
                dlugosc = j - i + 1
                if dlugosc > max_len:
                    max_len = dlugosc
                    wynik = slowo[i:j+1]
                break

    return wynik

slowo = ("bbbaaubueytwyetrywax")
print(MAXX(slowo))
