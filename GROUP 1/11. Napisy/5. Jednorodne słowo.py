napis = input()
n = len(napis)
c = 0
s = True
for i in range (0, n):
    if napis[0] != napis[i]:
        s = False

if s:
    print('TAK')
else:
    print('NIE')