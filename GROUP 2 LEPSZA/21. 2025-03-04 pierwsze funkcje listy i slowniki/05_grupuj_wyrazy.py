# 5. Napisz funkcję grupuj_wyrazy(wyrazy), która przyjmuje listę napisów i wypisze napisy pogrupowane wg długości.
# Np. dla grupuj_wyrazy(["dom", "pies", "kot", "samochód", "rower", "mata", "ala"]) wynikiem będzie coś w stylu:
# Napisy długości 3: dom kot ala
# Napisy długości 4: pies mata
# Napisy długości 5: rower
# Napisy długości 8: samochód

n = int(input())
lista = ["dom","pies","kot","samochod","rower","mata","ala"]
lista2 = []
lista3 = []

for i in lista:
    lista2.append(len(i))

print("lista wyrazow", lista)
print("lista dlugosci", lista2)
lista.sort()



lista2.sort()
for element in lista2:
    if element not in lista3:
        lista3.append(element)
print("lista rosnaca unikalnuch ",lista3)

for dlugosc in lista3:
    print(f"wyrazy o dlugosci {dlugosc}:")
    for wyraz  in lista:
        if len(wyraz) == dlugosc:
            print(wyraz)


owyrazy= {
    3:  ["ala","dom","kot"],
    4: ["mata","pies"],
    5: ["rower"]
}

slownik = dict()
def grupuj_wyrazy(lista):
    for wyraz in lista:
        dlugosc = len(wyraz)
        if dlugosc not in slownik:
            slownik[dlugosc] = []
        slownik[dlugosc].append(wyraz)
        print(f"wyraz: {wyraz} dlugosc: {dlugosc}")





grupuj_wyrazy(lista)
print(slownik)

for klucz, wartosc in slownik.items():
    print(f"klucz: {klucz}, wartosc: {" ".join(wartosc)}")
