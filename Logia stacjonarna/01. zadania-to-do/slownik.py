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
