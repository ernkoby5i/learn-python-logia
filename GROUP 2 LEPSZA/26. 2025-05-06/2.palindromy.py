#zadanie Palindromy - https://logia.oeiizk.waw.pl/logia/page.php?sr=logia11/2etap

def palindrom(s):
    wynik = 0
    for i in range(0,len(s)//2):
        pszud = i
        tyl = i+1
        wynik = wynik+1

        if s[-tyl] != s[pszud]:
            wynik = wynik+len(s)+1
            return wynik
    wynik = wynik + len(s)
    return wynik

s = 'mam'
print(palindrom(s))


