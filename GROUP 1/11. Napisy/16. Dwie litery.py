napis = input()
n = len(napis)

if n>2:
    if napis[0] == napis[2] and napis[1] == napis[3] and napis[0] != napis[1]:
        print("TAK")
    else:
        print("NIE")
else:
    if napis[0] != napis[1]:
        print("TAK")
    else:
        print("NIE")