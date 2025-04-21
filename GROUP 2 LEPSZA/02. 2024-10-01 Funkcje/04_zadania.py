# ile = ("ababcb")
n = "b"
def ile(text,n):
    wynik = 0
    for i in text:
        if i == n:
            wynik = wynik + 1

    return wynik
y = ile("ababcb", "b") # 3
print(y)

#czy(1,3,2)
x = 1
y = 3
z = 3

if z>=x and z<=y:
    print("TRUE")
else:
    print("FALSE")




def moj_max(x1,x2,x3):
    m = None
    k = max(x1,x2)
    m = max(k,x3)

    return m

print(moj_max(25544,1654,23456))


