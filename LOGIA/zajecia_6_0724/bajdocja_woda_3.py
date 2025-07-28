
#  @
#  @ ~ ~ ~ @ @
#  @ ~ ~ @ @ @ ~ @
#  @ @ @ @ @ @ @ @ @
#  0 1 2 3 4 5 6 7 8  - idx
# [4 1 1 2 3 3 1 2 1] - poziom_terenu

poziom_terenu = [4, 1, 1, 2, 3, 3, 1, 2, 1]
# pomijam pierwszy i ostatni bo tam woda sie nie zbiera.
# for i = 1..n-2 sprawdz boki max w lewo i max w prawo
# z obu max wybieram miniejszy i jezeli to jest wieksze od mojego poziomu idx to to jest ilosc wodu ktora sie zebrala
# przyklad: dla idx = 1
#           poziom_terenu(idx=1) = 1
#           max_na_lewo(1)  = 4
#           max_na_prawo(1) = 3
#           min(4,3) = 3
#           min(4,3) - poziom(idx=1) = 3 - 1 = 2
#           na pozycji idx=1 uzbiera sie slup wody o ilosci 2

def max_na_lewo(poziom_terenu, idx):
    # wez pierwszy w lewo od idx i idz dalej
    # jezeli taki sam albo rosnie to dalej
    # jak zaczyna malec to NIE KONCZ

    max_poziom_wody_w_lewo = poziom_terenu[idx]
    i = idx
    while i>0:
        i = i - 1
        if poziom_terenu[i]>max_poziom_wody_w_lewo:
            max_poziom_wody_w_lewo = poziom_terenu[i]

    return max_poziom_wody_w_lewo

def max_na_prawo(poziom_terenu, idx):
    # wez pierwszy w prawo od idx i idz dalej
    # jezeli taki sam albo rosnie to dalej
    # jak zaczyna malec to NIE KONCZ

    max_poziom_wody_w_prawo = poziom_terenu[idx]
    i = idx
    while i < len(poziom_terenu)-1:
        i = i + 1
        if poziom_terenu[i] > max_poziom_wody_w_prawo:
            max_poziom_wody_w_prawo = poziom_terenu[i]

    return max_poziom_wody_w_prawo

def ile_wody_w_idx(poziom_terenu, idx):
    max_left  = max_na_lewo(poziom_terenu, idx)
    max_right = max_na_prawo(poziom_terenu, idx)
    dolek = min(max_left, max_right) - poziom_terenu[idx]

    print(f"ile wody zatrzyma sie w idx={idx}. {max_left=} {poziom_terenu[idx]=} {max_right=} {dolek=}")

    if dolek>0:
        return dolek
    else:
        return 0

def ile_wody(poziom_terenu):
    dlugosc = len(poziom_terenu)


    # jezeli teren ma tylko < 2 punkty to woda nie ma gdzie sie zbierac.
    # musi byc minimum 3: np: 2,1,2
    if dlugosc<3:
        return 0

    total_woda = 0
    for idx in range(1, len(poziom_terenu) - 1):  # od 1 do len(l)-2
        total_woda = total_woda + ile_wody_w_idx(poziom_terenu, idx)

    return total_woda


print(f"teren = {poziom_terenu} {ile_wody(poziom_terenu)=}")

