# ta zmienna powie nam w trakcie spadania kolejnego liscia czy mamuy juz wszystko zakryte.
# nie musimuy w ten sposom nic sprawdzac.

def czy_ropucha_pokona_rzeke_dict(n_pozycji,m_lisci,lista):
    zakryte_pozycje = 0
    ile_liscie_na_pozycji = dict()
    iRet = -1
    cnt = 0
    for pozycja_liscia in lista:
        cnt = cnt + 1
        if not (1 <= pozycja_liscia <= n_pozycji):
            print(f"{pozycja_liscia} spoza zakresu. continue")
            continue
        x = ile_liscie_na_pozycji.get(pozycja_liscia,0)
        ile_liscie_na_pozycji[pozycja_liscia] = x+1
        if x == 0:
            zakryte_pozycje += 1
            if zakryte_pozycje == n_pozycji:
                iRet = cnt
                break
    print(ile_liscie_na_pozycji)
    return iRet

def czy_ropucha_pokona_rzeke_arr(n_pozycji,m_lisci,lista):
    zakryte_pozycje = 0
    arr = [0]* (n_pozycji+1)
    iRet = -1
    cnt = 0
    for pozycja_liscia in lista:
        cnt = cnt + 1
        if not (1 <= pozycja_liscia <= n_pozycji):
            print(f"{pozycja_liscia} spoza zakresu. continue")
            continue
        x = arr[pozycja_liscia]
        arr[pozycja_liscia] = x + 1
        if x == 0:
            zakryte_pozycje += 1
            if zakryte_pozycje == n_pozycji:
                iRet = cnt
                break
    print(arr)
    return iRet


iRet = czy_ropucha_pokona_rzeke_dict(5,8, [1, 3, 1, 4, 2, 3, 5, 4])
print(iRet)

iRet = czy_ropucha_pokona_rzeke_arr(5,8, [1, 3, 1, 4, 2, 3, 5, 4])
print(iRet)