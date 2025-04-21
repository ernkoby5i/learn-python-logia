n = int(input())
l1 = []

for e in range (1, 11):
    l1.append(0)

l2 = list(map(int, input().split()))

for e in l2:
    l1[e] = l1[e] + 1

print(" ".join(map(str, l1)))

