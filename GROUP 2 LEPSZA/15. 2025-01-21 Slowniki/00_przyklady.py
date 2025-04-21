# 15. 21.01.2025 https://codeshare.io/w9xzjp Slownik                        [BARDZO WAZNE]
# dict(ionary), czyli słownik przechowuje pary (klucz: wartość)
slownik = {'ewa': 21, 'mateusz': 22, 'nadia': 20}
pusty_slownik = dict()

# sprawdzanie wartości w słowniku
print(slownik['ewa'])

print(slownik)
# dodawanie do słownika
slownik['bartek'] = 23
print(slownik)

# sprawdzenie czy coś jest w słowniku
print('kamil' in slownik)
# jak jakiegoś klucza nie ma to dostaniemy błąd
# slownik['kamil']

# zamiast tego możemy użyć funkcji get(), która w takim
# przypadku zwróci None
print(slownik.get('kamil'))


# możemy też nadpisywać stare wartości tak samo jak dodajemy
slownik['bartek'] = 33
print(slownik['bartek'])

# usuwamy za pomocą funkcji pop
slownik.pop('bartek')

print(slownik)
print(len(slownik))  # wypisze liczbę par w słowniku


ososby_i_przedmiioty = {
    'ewa': ["matematyka","polski"],
    'mateusz': ["matematyka","polski","niemiecki"],
    'nadia': ["matematyka"],
}

print(ososby_i_przedmiioty)