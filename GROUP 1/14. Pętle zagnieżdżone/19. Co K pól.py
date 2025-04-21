l1 = list(map(int, input().split()))
#n = 5
l2 = list(map(int, input().split()))
#l2 = [1,3,-9,8,7]

#k = 3
naj = None

n = l1[0]
k = l1[1]


def sprawdz(i,k):
    global naj
    c = 0
    for j in range(i,n,k):
        #print(f'wynosi indrx {j}')
        if i<n:
            c = c+l2[j]
            if naj is None:
                naj = c
            else:
                if naj < c:
                    naj = c

    return naj

for x in range(0,len(l2)-1):
    #print(f'szukam dla x = {x} wynik to = {sprawdz(x,k)} ')
    y = sprawdz(x,k)

print(naj)

































