s1 = list(input())
n = len(s1)
c = 0
s = 1

for i in range(0, n):
    if s1[i] == 'A':
        c = i
        break

for i in range(1, n):
    if s1[-i] == 'A':
        s = i
        break
g = n-s
print(f'pierwsze A: {c}')
print(f'ostatnie A: {g}')
print(f'odleglosc A: {g-c}')


