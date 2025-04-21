n = int(input())
k = int(input())
l1 = list(map(int, input().split()))
a = 0
b = 1
for i in range(1, k+1):
    suma = l1[a] + l1[b]
    l1.append(suma)
    l1.pop(0)
    l1.pop(0)
    print(l1)

print(l1)