def bajtek_max_strata(gielda):
    naj = 0
    bierzonca = 0
    for liczba in(gielda):
        bierzonca = bierzonca+liczba
        if bierzonca<naj:
            naj = bierzonca
        if bierzonca>0:
            bierzonca = 0

    #return abs(naj)
    return naj

def bajtek_najlepsza_trasa(gielda):
    max_strata = bajtek_max_strata(gielda)
    suma_na_calej_trasie = sum(gielda)
    przejazd_bez_zarobku = 0
    przejazd_bez_max_strata = max(suma_na_calej_trasie+max_strata,0)
    przejazd_w_kolko = suma_na_calej_trasie*2
    najlepsza_trasa = max(przejazd_bez_zarobku,przejazd_bez_max_strata,przejazd_w_kolko)
    print(gielda)
    print(f' {max_strata=}')
    print(f' {suma_na_calej_trasie=}')
    print(f' {przejazd_bez_zarobku=}')
    print(f' {przejazd_bez_max_strata=}')
    print(f' {przejazd_w_kolko=}')
    print(f'najlepsza_trasa {najlepsza_trasa}')
    return najlepsza_trasa


trasa = [-1,-1]
print(bajtek_najlepsza_trasa(trasa))

trasa = [3 ,5 ,5 ,2]
print(bajtek_najlepsza_trasa(trasa))

trasa = [14,-6,8,-8,9,3,-1]
print(bajtek_najlepsza_trasa(trasa))