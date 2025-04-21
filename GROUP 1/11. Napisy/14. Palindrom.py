s1 = input()
n = len(s1)
j = 1
c = 0
for i in s1:
    if i == s1[-j]:
        c = c+1
    else:
        break
    j = j+1

if n == c:
    print('TAK')
else:
    print('NIE')