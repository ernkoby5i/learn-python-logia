#zadanie Bieg - https://logia.oeiizk.waw.pl/logia/page.php?sr=logia15/1etap

def bieg(s):
    poprzednia = None
    wynik = 0
    najwynik = 0
    for i in range(0,len(s)):
        if i!=0:
            poprzednia = s[i-1]

        if s[i]==poprzednia:
            wynik = wynik+1

        if wynik>najwynik:
            najwynik = wynik
    return wynik

s = (1,3,3,5,5,4,4,5,4,4)
print(bieg(s))
