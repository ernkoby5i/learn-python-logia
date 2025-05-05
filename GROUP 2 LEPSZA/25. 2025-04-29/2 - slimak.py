# Drugie - Ślimak https://logia.oeiizk.waw.pl/logia/page.php?sr=logia13/2etap


def kiedy(wchodze,spadam,belka):
    jestem_na = 0
    day = 0
    last = 0
    while True:
        if jestem_na>=1000:
            return day
        last = (jestem_na//belka)*belka

        if day!=0:
            jestem_na = jestem_na - spadam
        if jestem_na<last:
            jestem_na = last

        jestem_na = jestem_na+wchodze
        day = day+1

print(kiedy(5, 3, 2))


