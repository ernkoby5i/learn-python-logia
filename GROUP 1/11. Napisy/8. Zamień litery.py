napis = input()
n = len(napis)

for i in range(0, n-1, 2):
    a = napis[i]
    b = napis[i+1]
    print(b+a,end='')

if (n % 2 != 0):
    print(napis[n-1])