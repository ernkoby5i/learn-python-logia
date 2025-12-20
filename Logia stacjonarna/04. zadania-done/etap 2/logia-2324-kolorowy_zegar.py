G, M = input().split()
G = int(G)
M = int(M)
print(G,M)
KG = G%4
KM = M%5

if KG==0:
    KG = 'czerwony'
if KG==1:
    KG = 'zielony'
if KG==2:
    KG = 'niebieski'
if KG==3:
    KG = 'fioletowy'
if KM == 0:
    KM = 'zielony'
if KM == 1:
    KM = 'niebieski'
if KM == 2:
    KM = 'fioletowy'
if KM == 3:
    KM = 'czerwony'
if KM == 4:
    KM = 'pomaranczowy'




c = 0
while True:
    if KM == 0:
        KM = 'zielony'
    if KM == 1:
        KM = 'niebieski'
    if KM == 2:
        KM = 'fioletowy'
    if KM == 3:
        KM = 'czerwony'
    if KM == 4:
        KM = 'pomaranczowy'
    if KM==KG:
        print(c)
        break

    M = M+1
    KM = M % 5
    if M==60:
        M = 0
        G = G+1

        KG = G % 4
        KM = M % 5

        if KM == 0:
            KM = 'zielony'
        if KM == 1:
            KM = 'niebieski'
        if KM == 2:
            KM = 'fioletowy'
        if KM == 3:
            KM = 'czerwony'
        if KM == 4:
            KM = 'pomaranczowy'


        if KG == 0:
            KG = 'czerwony'
        if KG == 1:
            KG = 'zielony'
        if KG == 2:
            KG = 'niebieski'
        if KG == 3:
            KG = 'fioletowy'

    c = c+1

