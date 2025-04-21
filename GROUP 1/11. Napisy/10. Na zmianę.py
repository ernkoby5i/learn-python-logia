napis = input()
n = len(napis)

if n%2==0:
    x = -1
    d = 0
    for i in range (0, n//2):
        #print(i)
        print(napis[d],end="")
        print(napis[x],end="")
        x = x - 1
        d = d+1
else:
    x = -1
    d = 0
    print(napis[d], end="")
    d = d+1
    for i in range (0, n//2):
        #print(i)
        print(napis[x], end="")
        print(napis[d],end="")
        x = x - 1
        d = d+1