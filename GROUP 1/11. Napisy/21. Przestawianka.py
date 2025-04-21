s1 = list(input())
n = int(input())
print(s1)

for i in range(0,n):
    pierwszy_element = s1.pop(0)
    s1.append(pierwszy_element)


for i in s1:
    print(i,end='')
