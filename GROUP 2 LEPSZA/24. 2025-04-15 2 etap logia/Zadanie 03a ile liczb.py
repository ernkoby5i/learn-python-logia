# Ile liczb - https://logia.oeiizk.waw.pl/logia/page.php?sr=logia15/2etap

# opcja 1
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


# Opcja 2: z rekurencja
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


# opcja 3: (mniej kodu)
def ile4(n,cyfra):
    wynik = None
    if cyfra != 0:
        if n == 1: return 1
        wszystkie = 10 ** n                                  # [0..9] [0..9] [0..9] n dowolnych cyfr       009
        wszystkie_dobra  = 9*10**(n-1)                       # [1..9] [0..9] [0..9] n cyfr ale nie od 0    109
        bez_1_cyfry      = 9**n                              # [0..8] [0..8] [0..8]
        ilosc_bez_liczby_z_zero = 8*9**(n-1)                 # [1..8] [0..8] [0..8] 108
        wynik = wszystkie_dobra - ilosc_bez_liczby_z_zero

    if cyfra == 0:
        if n == 1: return 0
        wszystkie = 10**n                 # [0..9] [0..9] [0..9] n cyfr
        wszystkie_dobra = 9 * 10**(n-1)   # [1..9] [0..9] [0..9] musza miec n cyfr i nie moga zaczunac sie od 0
        bez_zero        = 9**n            # [1..9] [1..9] [1..9] nie maja 0
        wynik = wszystkie_dobra - bez_zero
    return wynik




# Opcja 4
def ile4(n,cyfra):
    wszystkie       = 10 ** n               # [0..9] [0..9] [0..9] n dowolnych cyfr       009
    wszystkie_dobra = 9 * 10 ** (n - 1)     # [1..9] [0..9] [0..9] n cyfr ale nie od 0    109

    wynik = None
    if cyfra != 0:
        bez_1_cyfry      = 9**n                              # [0..8] [0..8] [0..8]
        ilosc_bez_liczby_z_zero = 8*9**(n-1)                 # [1..8] [0..8] [0..8] 108
        wynik = wszystkie_dobra - ilosc_bez_liczby_z_zero

    if cyfra == 0:
        bez_zero        = 9**n            # [1..9] [1..9] [1..9] nie maja 0
        wynik = wszystkie_dobra - bez_zero
    return wynik






n_cyfr = 1
cyfra  = 0


wynik = f(n_cyfr,cyfra)
print(f"{wynik=}")

wynik = ile_liczb_bez_zero_na_pierwszej_pozycji(n_cyfr, cyfra)
print(f"{n_cyfr=} {cyfra=} {wynik=}")
print(f"WYNIK 1 = {wynik}")

wynik = ile(n_cyfr,cyfra)
print(f"WYNIK 2 = {wynik}")
