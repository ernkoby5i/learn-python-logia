n = int(input())
odpowidz = -1

for i in range (100,1000):
    a = i//100
    b = (i-a*100)//10
    c = i-a*100-b*10
    if(a+b+c==n):
        odpowidz = i
        break

print(odpowidz)