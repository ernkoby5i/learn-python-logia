# Ile liczb - https://logia.oeiizk.waw.pl/logia/page.php?sr=logia15/2etap
def f(a,b):
    start  = 10**(a-1)

    wynik = 0
    end = 10**a-1

    print(f"{start=} {end=}")
    for i in range(start,end+1):
        w = str(i)
        #print(w)
        for d in w:
            if d == str(b):
                #print("mam")
                wynik = wynik+1

                break
    return wynik



#wynik = f(9,3)
#print(f"{wynik=}")





def ile(n,cyfra):
    if cyfra != 0:
        wynik = 9*10**(n-1)-8*9**(n-1)
    if cyfra==0:
        wynik = 9*10**(n-1)-9**n

    return wynik

print(ile(9,9))