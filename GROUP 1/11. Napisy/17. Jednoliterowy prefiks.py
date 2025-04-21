napis = input()
n = len(napis)

if n == 0:
    print("")
else:

    prefiks = napis[0]
    for i in range(1, n):
        if napis[i] == napis[0]:
            prefiks += napis[i]
        else:
            break

    print(prefiks)