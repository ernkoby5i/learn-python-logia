# zawsze musimy zaplacic temu ktory jest pierwszy w kolejce przy kasie
# potam cofamy sie wstecz i szukamy kazdego kto chce miniej od niego.
# zauwazmy ze  z,z,z,1,2,y,y,2,x1,x2,x3,3
# jezeli jestesmy na drugiej 2 i x1, x2, x3 kazdy jest wiekszy od 3 to nie oplaca nam sie tam skakac i wykonamy skok na 3
# jednoczenise z 1 nie oplaca sie skoczyc na pierwsza napotkana 2 jezeli mozemy skocznyc od razu do przodu na druga.
# to pokazuje ze mozemy sie cofac od 3 wsteecz i szukac pierwszej napotkanej liczby miniejszej od 3
# wtedy ona staje sie nasza ostatnia pozycja na ktora trzeba wskoczyc i uzyc tej ceny.
# wiec cofamy sie wstecz szukajac pierwszej mniejszej etc.
# a to wszysko wynika z tego ze:   [bytek, x, y, z] wtedy
# jezeli x = y to
#  bytek -> x skok_x = 1 * x         = x
#  bytek -> y skok_y = 1 * y = 1 * x = x (tyle samo a jestesmy blizej kasy)
# jezeli y = x - 1 oraz z = x - 1 to:
#  bytek -> x -> y skok_x + 1 * y = (1*x) + [1 * (x-1)] =  x + x - 1 = 2x - 1 (drozej)
#  bytek -> y      skok_y = 2 * y = 2 * (x-1)                        = 2x - 2 (taniej)
# albo
#  bytek -> y -> z skok_y + 1*z = 2x-2 + (x-1) = 3x - 3
#  bytek -> z      skok_z = 3 * z = 3 * (x-1)  = 3x - 3 (tyle a jestemy blizej)
# Dlatego szukamy najnizszej wartosci jak najdalej do przodu.( a jak sa 2 takie same to wybieramy ta dalsza)


# pierwsze podejscie w jednej iteracji wyznaczymy indexy a w drugiej liczymy total_cost
def do_cukierni_1(lista_ludzi_z_cenami):
    print("-----------------------------------------------")
    print(f"Lista ludzi z cenami {lista_ludzi_z_cenami} v1")
    stos_cen_reverse=[]
    stos_idx_reverse=[]
    ostatni_koszt = 0
    ostatni_idx = 0
    # specjalne przypadki
    if len(lista_ludzi_z_cenami) == 0:
        return 0

    ostatni_idx = len(lista_ludzi_z_cenami) -1
    ostatni_koszt = lista_ludzi_z_cenami[ostatni_idx]
    stos_cen_reverse.append(ostatni_koszt)
    stos_idx_reverse.append(ostatni_idx)
    while ostatni_idx>0:
        ostatni_idx = ostatni_idx - 1
        if lista_ludzi_z_cenami[ostatni_idx]<ostatni_koszt:
            ostatni_koszt = lista_ludzi_z_cenami[ostatni_idx]
            stos_cen_reverse.append(ostatni_koszt)
            stos_idx_reverse.append(ostatni_idx)
    i = 0

    print(f"JA(0),", end="")
    while i<len(lista_ludzi_z_cenami):
        print(f"{lista_ludzi_z_cenami[i]}({i+1})",end="")
        if i in stos_idx_reverse:
            print("*", end="")
        print(",", end="")
        i = i+1
    print("\n")


    total_koszt = 0
    my_idx=-1
    i = len(stos_idx_reverse)-1
    while i >= 0:
        my_next_idx  = stos_idx_reverse[i]
        my_next_cost = stos_cen_reverse[i]
        delta_idx = my_next_idx - my_idx
        print(f'jump {delta_idx} from {my_idx+1} to {my_next_idx+1} for {delta_idx * my_next_cost} USD')
        my_idx = my_next_idx
        total_koszt = total_koszt + delta_idx * my_next_cost
        i = i - 1

    return total_koszt

# drugie podejscie w trakcie przeszukiwania obliczamy koszt (bo wiemy gdzie ma wyladowac i skad)
# kod mozna uproscic ale tak jest specjalnie zeby bylo czytelniej
def do_cukierni_2(lista_ludzi_z_cenami):
    print("-----------------------------------------------")
    print(f"Lista ludzi z cenami {lista_ludzi_z_cenami} v2" )
    stos_cen_reverse=[]
    stos_idx_reverse=[]

    if len(lista_ludzi_z_cenami) == 0:
        return 0

    total_koszt = 0

    ostatni_idx = len(lista_ludzi_z_cenami) -1
    last_bajtek_idx = ostatni_idx
    ostatni_koszt = lista_ludzi_z_cenami[ostatni_idx]
    stos_cen_reverse.append(ostatni_koszt)
    stos_idx_reverse.append(ostatni_idx)
    while ostatni_idx>0:
        nastepny_idx = ostatni_idx - 1
        if lista_ludzi_z_cenami[nastepny_idx]<ostatni_koszt:
            nowy_koszt = lista_ludzi_z_cenami[nastepny_idx]
            stos_cen_reverse.append(nowy_koszt)
            stos_idx_reverse.append(nastepny_idx)
            koszt_przejscia = (last_bajtek_idx - nastepny_idx) * ostatni_koszt
            print(f"{koszt_przejscia=}")
            ostatni_koszt = nowy_koszt
            total_koszt  = total_koszt + koszt_przejscia

            last_bajtek_idx = nastepny_idx
        ostatni_idx = nastepny_idx

    pierwsza_pozycja_bajtka = -1
    koszt_przejscia = (last_bajtek_idx - pierwsza_pozycja_bajtka) * ostatni_koszt
    print(f"{koszt_przejscia=}")
    total_koszt = total_koszt + koszt_przejscia


    i = 0
    print(f"JA(0),", end="")
    while i<len(lista_ludzi_z_cenami):
        print(f"{lista_ludzi_z_cenami[i]}({i+1})",end="")
        if i in stos_idx_reverse:
            print("*", end="")
        print(",", end="")
        i = i+1
    print("\n")

    # total_koszt = 0
    # my_idx=-1
    # i = len(stos_idx_reverse)-1
    # while i >= 0:
    #     my_next_idx  = stos_idx_reverse[i]
    #     my_next_cost = stos_cen_reverse[i]
    #     delta_idx = my_next_idx - my_idx
    #     print(f'jump {delta_idx} from {my_idx+1} to {my_next_idx+1} for {delta_idx * my_next_cost} USD')
    #     my_idx = my_next_idx
    #     total_koszt = total_koszt + delta_idx * my_next_cost
    #     i = i - 1


    return total_koszt


# 3 podejscie upraszzam kod nie musz juz pamietac historii. bo na biezaco licze.
# tablica tez byla potrzebna aby ladnie wydrukowac.
def do_cukierni_3(lista_ludzi_z_cenami):
    print("-----------------------------------------------")
    print(f"Lista ludzi z cenami {lista_ludzi_z_cenami} v3")

    if len(lista_ludzi_z_cenami) == 0:
        return 0

    total_koszt = 0

    idx = len(lista_ludzi_z_cenami) -1
    last_bajtek_idx = idx
    ostatnia_cena = lista_ludzi_z_cenami[idx]
    while idx>0:
        idx = idx - 1
        if lista_ludzi_z_cenami[idx]<ostatnia_cena:
            skok = (last_bajtek_idx - idx)
            total_koszt  = total_koszt + skok * ostatnia_cena
            ostatnia_cena = lista_ludzi_z_cenami[idx]
            last_bajtek_idx = idx

    skok = (last_bajtek_idx + 1)
    total_koszt = total_koszt + skok * ostatnia_cena

    return total_koszt

########## MAIN ##########################

lista_ludzi_z_cenami = []
print(f'WYNIK : trzeba zaplacic {do_cukierni_1(lista_ludzi_z_cenami)=} USD')

lista_ludzi_z_cenami = [2]
print(f'WYNIK : trzeba zaplacic {do_cukierni_1(lista_ludzi_z_cenami)=} USD')

lista_ludzi_z_cenami = [7, 1, 5, 3, 2, 6, 4]
print(f'WYNIK : trzeba zaplacic {do_cukierni_2(lista_ludzi_z_cenami)=} USD')

lista_ludzi_z_cenami = [7, 1, 5, 2, 2, 1, 4]
print(f'WYNIK : trzeba zaplacic {do_cukierni_2(lista_ludzi_z_cenami)=} USD')



lista_ludzi_z_cenami = []
print(f'WYNIK : trzeba zaplacic {do_cukierni_3(lista_ludzi_z_cenami)=} USD')

lista_ludzi_z_cenami = [2]
print(f'WYNIK : trzeba zaplacic {do_cukierni_3(lista_ludzi_z_cenami)=} USD')

lista_ludzi_z_cenami = [7, 1, 5, 3, 2, 6, 4]
print(f'WYNIK : trzeba zaplacic {do_cukierni_3(lista_ludzi_z_cenami)=} USD')

lista_ludzi_z_cenami = [7, 1, 5, 2, 2, 1, 4]
print(f'WYNIK : trzeba zaplacic {do_cukierni_3(lista_ludzi_z_cenami)=} USD')