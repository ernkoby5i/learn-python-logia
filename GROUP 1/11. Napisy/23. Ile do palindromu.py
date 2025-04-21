s1 = list(input())
n = len(s1)
c = 0
g = 1

for i in range(0, n):
    if s1[i]!=s1[-g]:
        c = c+1
    g = g+1

print(c//2)