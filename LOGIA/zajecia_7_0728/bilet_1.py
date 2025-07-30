def bajtek_max_zysk(odcinki):
    max_sum = 0
    zarobek_od_startu = 0
    for x in odcinki:

        zarobek_od_startu = zarobek_od_startu + x
        if zarobek_od_startu < 0:
            zarobek_od_startu = 0


        if zarobek_od_startu > max_sum:
            max_sum = zarobek_od_startu

    return max_sum


lista_dochodow_na_odcinkach=[-1, -1]
print(f'{lista_dochodow_na_odcinkach} {bajtek_max_zysk(lista_dochodow_na_odcinkach)=}')

lista_dochodow_na_odcinkach=[1, 2, 3]
print(f'{lista_dochodow_na_odcinkach} {bajtek_max_zysk(lista_dochodow_na_odcinkach)=}')

lista_dochodow_na_odcinkach=[1, 2, -1, 3]
print(f'{lista_dochodow_na_odcinkach} {bajtek_max_zysk(lista_dochodow_na_odcinkach)=}')