napis = input()
n = len(napis)
c = 0
o = 0
r = 0
for i in napis:
    if i == "R":
        r = r+1
    else:
        o = o+1


if(o<r):
    print(o)
else:
    print(r)