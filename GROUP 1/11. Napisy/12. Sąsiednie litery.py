napis = input()
n = len(napis)
c = 0
poprzednia = 0

for i in napis:
    if poprzednia == i:
        c = c+1
    poprzednia = i
print(c)