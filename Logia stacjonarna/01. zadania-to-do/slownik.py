slownik = {
    'a':0,
    'b':0,
}

for key in slownik:
    print(f'Key: {key}, Value: {slownik[key]}')

lista = ['a','a','b','a','b','b','a', 'c','c','c','a']
for item in lista:
    if item in slownik:
        slownik[item] += 1
    else:
        slownik[item] = 1


print(slownik)


tekst = 'aaabbbaddc'
#tekst = input()
llista = list(tekst)

slownik = {}

for i in llista:
    if i in slownik.keys():
        slownik[i] = slownik[i]+1
    else:
        slownik[i] = 1
print("---")
print(f"{len(slownik)} {tekst} len={len(tekst)}")
print(slownik)

palindrom_dlugosc = 0
palindorm_polowa=''

for key in slownik.keys():
    if slownik[key]>1:
        dobre_litery = (slownik[key] // 2)
        for i in range(dobre_litery):
            palindorm_polowa += key
        palindrom_dlugosc += dobre_litery *2
        slownik[key] = slownik[key] - dobre_litery*2

palindorm_srodek=''
print(slownik)
print(f"{palindrom_dlugosc=}")
for key in slownik.keys():
    if slownik[key]>0:
        palindrom_dlugosc += 1
        palindorm_srodek = key
        break

palindorm = palindorm_polowa + palindorm_srodek + palindorm_polowa[::-1]
palindrom_dlugosc_final = len(palindorm)
print(f"{palindorm=} {palindrom_dlugosc_final=}")
print(slownik)
print(f"")
