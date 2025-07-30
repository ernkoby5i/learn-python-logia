def nasza_waga(wagi):
    if len(wagi)<=1:
        return 0

    max_waga = wagi[0]
    max_schudnuecie = 0

    for waga in wagi[1:]: # zapis wagi[1:] bierze on [1..n-1] bo [0] mamy juz wykorzystany
        if waga>max_waga:
            max_waga = waga
        if (max_waga-waga)>max_schudnuecie:
            max_schudnuecie = (max_waga-waga)
    return max_schudnuecie


wagi = [6, 7, 5, 4, 2]
print(wagi,nasza_waga(wagi))

wagi = [90, -90, 111, 4, 12]
print(wagi,nasza_waga(wagi))

wagi = [1,2,0]
print(wagi,nasza_waga(wagi))
