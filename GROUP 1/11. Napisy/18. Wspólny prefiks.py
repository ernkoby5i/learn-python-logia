s1 = input()
s2 = input()
n = min(len(s1), len(s2))

x=0
for i in range(n):
    if s1[i]==s2[i]:
        x = x +1
    else:
        break

print(x)