# Ile liczb - https://logia.oeiizk.waw.pl/logia/page.php?sr=logia15/2etap
# 1 propozycja z rekurencja
def ile_liczb_includng_zero_na_pierwszej_pozycji(n):
    if n == 1:
        wynik = 1
        print(f"ile_liczb_includng_zero_na_pierwszej_pozycji({n})")
        print(f'{wynik=}')
        return 1
    poprzedni_wynik = ile_liczb_includng_zero_na_pierwszej_pozycji(n-1)
    wynik = 1 * 10 ** (n - 1) + 9 * poprzedni_wynik
    print(f"ile_liczb_includng_zero_na_pierwszej_pozycji({n})")
    print(f"Dla {n=}: 1*{10**(n-1)} + 9 *  {poprzedni_wynik=} = {wynik=}")
    print(f'{wynik=}')
    return wynik

def ile_liczb_bez_zero_na_pierwszej_pozycji(n,cyfra):
    if n == 1:
        if cyfra == 0:
            return 0
        else:
            return 1

    poprzedni_wynik = ile_liczb_includng_zero_na_pierwszej_pozycji(n-1)
    wynik = 0
    if cyfra != 0:
        wynik = 1 * 10 ** (n - 1) + 8 * poprzedni_wynik
    else:
        wynik = 0 * 10 ** (n - 1) + 9 * poprzedni_wynik
    print(f"ile_liczb_bez_zero_na_pierwszej_pozycji({n},{cyfra})")
    print(f"Dla {n=}: 1*{10**(n-1)} + 8 *  {poprzedni_wynik=} = {wynik=}")
    return wynik


def f(a,b):
    start  = 10**(a-1)

    wynik = 0
    end = 10**a-1

    print(f"{start=} {end=}")
    for i in range(start,end+1):
        w = str(i)
        #print(w)
        for d in w:
            if d == str(b):
                #print("mam")
                wynik = wynik+1

                break
    return wynik



n_cyfr = 6
cyfra  = 4


wynik = f(n_cyfr,cyfra)
print(f"{wynik=}")

wynik = ile_liczb_bez_zero_na_pierwszej_pozycji(n_cyfr, cyfra)
print(f"{n_cyfr=} {cyfra=} {wynik=}")
print(f"WYNIK = {wynik}")
