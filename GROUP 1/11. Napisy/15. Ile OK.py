napis = input()
wynik = 0
for i in range(len(napis) - 1):
    if napis[i] == "O" and napis[i + 1] == "K":
        wynik += 1
print(wynik)