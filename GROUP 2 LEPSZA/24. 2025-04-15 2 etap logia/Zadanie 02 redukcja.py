# Redukcja - https://logia.oeiizk.waw.pl/logia/page.php?sr=logia15/2etap LOGIA 15 II ETAP

def redukcja (l):
    while True:
        i = len(l)-1
        znaleziona = False
        while i>=1:
            #print(l,i)
            b = l[i]
            a = l[i-1]
            if a==b:
                l.pop(i)
                l[i-1] = (a+b)%10
                znaleziona = True
                i = i-2
            else:
                i = i-1
        if znaleziona == False:
            break

liczba = int(input())
l = [int(cyfra) for cyfra in str(liczba)]



redukcja(l)
#print(l)
for i in l:
    print(i,end="")