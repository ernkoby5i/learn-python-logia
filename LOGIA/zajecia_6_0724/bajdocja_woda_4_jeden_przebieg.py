
#  @
#  @ ~ ~ ~ @ @
#  @ ~ ~ @ @ @ ~ @
#  @ @ @ @ @ @ @ @ @
#  0 1 2 3 4 5 6 7 8  - idx
# [4 1 1 2 3 3 1 2 1] - poziom_terenu

poziom_terenu = [4, 1, 1, 2, 3, 3, 1, 2, 1]
# idziemy do przodu i monitorujemy wzniesienia i spadki +1 -1
# nawet nas nie interesuje ze zaczynamy z 4 tylko nas interesuje ze jest -3. (moe byc depresja nawet)
# jak jest do gory to znaczy ze zamuka nam sie jakis dolek.
# wtedy zdejmujemy ze stosu (chyba index) gnie bylo obnizenie.
# jak mamy index obnizenia i index w gore to liczymy pole


def ile_wody(poziom_terenu):
    total_woda = 0
    stos_obnizenie_terenu = []
    idx = 0
    if len(poziom_terenu)==0:
        return 0

    last_poziom = poziom_terenu[0]
    while idx < len(poziom_terenu)-1:
        idx = idx + 1
        new_poziom = poziom_terenu[idx]
        if new_poziom<last_poziom:
            # odkladamy idx na stos tyle razy ile w dol
            for i in range(last_poziom- new_poziom):
                stos_obnizenie_terenu.append(idx)
        if new_poziom>last_poziom:
            # podnosimy ze stosu i zliczamy dlugosc.
            for i in range(new_poziom-last_poziom):
                # moze nic nie byc na stos
                if len(stos_obnizenie_terenu)>0:
                    idx_obizenia = stos_obnizenie_terenu.pop(-1)
                    dlugosc=idx-idx_obizenia
                    total_woda = total_woda + dlugosc
        last_poziom = new_poziom

    return total_woda

# WERSJA Z DODAKOWYM PRINT do debugownia
def ile_wody_debug(poziom_terenu):
    dlugosc_terenu = len(poziom_terenu)
    if dlugosc_terenu<3:
        return 0

    total_woda = 0
    stos_obnizenie_terenu = []
    idx = 0
    last_poziom = poziom_terenu[0]
    while idx < len(poziom_terenu)-1:
        print("--------------------------------")
        idx = idx + 1
        new_poziom = poziom_terenu[idx]
        print(f"sprawdzam {idx=} {last_poziom} -> {new_poziom} {stos_obnizenie_terenu}")
        if new_poziom<last_poziom:
            for i in range(last_poziom- new_poziom):
                print(" idziemy DOWN. na stos i zmniejsz o -1")
                stos_obnizenie_terenu.append(idx)
        if new_poziom>last_poziom:
            for i in range(new_poziom-last_poziom):
                print(f" idziemy UP. zdejmij ze stos 1 {stos_obnizenie_terenu}")
                if len(stos_obnizenie_terenu)>0:
                    idx_obizenia = stos_obnizenie_terenu.pop(-1)
                    dlugosc=idx-idx_obizenia
                    total_woda = total_woda + dlugosc
                    print(f"{dlugosc=}")
                else:
                    print("nie ma nic na stosie.")
        if new_poziom==last_poziom:
            print(" no chanage")
        print(f"STOS STOP  : {stos_obnizenie_terenu}")
        print("--------------------------------")
        last_poziom = new_poziom

    return total_woda


print(f"teren = {poziom_terenu} {ile_wody(poziom_terenu)=}")

poziom_terenu = [1, 3, 4, 2, 3, 5, 2, 3, 2, 1, 2]
print(f"teren = {poziom_terenu} {ile_wody(poziom_terenu)=}")

poziom_terenu = [4, 1, 1, 2, 3, 3, -1, 2, 1] # depresja
print(f"teren = {poziom_terenu} {ile_wody(poziom_terenu)=}")

poziom_terenu = [1]
print(f"teren = {poziom_terenu} {ile_wody(poziom_terenu)=}")

poziom_terenu = [1,1]
print(f"teren = {poziom_terenu} {ile_wody(poziom_terenu)=}")

poziom_terenu = [1,0,1]
print(f"teren = {poziom_terenu} {ile_wody(poziom_terenu)=}")

poziom_terenu = []
print(f"teren = {poziom_terenu} {ile_wody(poziom_terenu)=}")
