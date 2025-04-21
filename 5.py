l = input()
def funkcja(l):
    wynik = 0
    for i in l:
        if i!=" ":
            wynik = wynik + ord(i)
    return wynik

print(funkcja(l))