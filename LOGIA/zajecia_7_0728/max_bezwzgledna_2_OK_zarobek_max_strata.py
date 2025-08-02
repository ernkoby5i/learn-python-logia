def bajtek_max_zarobek(gielda):
    naj = 0
    bierzonca = 0
    for liczba in(gielda):
        bierzonca = bierzonca+liczba
        if bierzonca>naj:
            naj = bierzonca
        if bierzonca<0:
            bierzonca = 0

    return naj

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

def bajtek_max_abs(gielda):
    max_zarobek = bajtek_max_zarobek(gielda)
    max_strata = bajtek_max_strata(gielda)
    max_abs = max(abs(max_strata),abs(max_zarobek))
    return max_abs





gielda = [1, -3, 2, 3, -4]
print(f'bajtek zarobek = {bajtek_max_zarobek(gielda)}')
print(f'bajtek strata = {bajtek_max_strata(gielda)}')
print(f'bajtek abs = {bajtek_max_abs(gielda)}')

print('')

gielda = [2, -5, 1, -4, 3, -2]
print(f'bajtek zarobek = {bajtek_max_zarobek(gielda)}')
print(f'bajtek strata = {bajtek_max_strata(gielda)}')
print(f'bajtek abs = {bajtek_max_abs(gielda)}')