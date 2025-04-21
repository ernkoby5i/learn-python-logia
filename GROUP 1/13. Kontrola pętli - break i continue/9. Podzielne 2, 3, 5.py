n = int(input())
s1 = list(map(int, input().split()))
c = 0
for i in s1:
    if (i%2==0 or i%3==0 or i%5==0) and not(i%2==0 and i%3==0 and i%5==0):
        c = c+1
print(c)