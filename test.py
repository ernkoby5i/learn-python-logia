# informacje = [20, "Adam", 10, 20, "Ewa", True]
# dlugosc = len(informacje)
# print(dlugosc)
#
# print(informacje[-7])

l = ['a','b','c','d']

l = ['a','b']

n = len(l)
beg = 0
end = 2
for i in range(beg,end+1):
    if i<=len(l)-1:
        print(i)

print("-----")

beg = n-3
end = n-1
for i in range(beg,end+1):
    print(i)
