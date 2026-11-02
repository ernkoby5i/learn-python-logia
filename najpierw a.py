def sprawdzanie(napis):
    skrot = []
    for i in napis:
        skrot.append(i)
        roznice = 0
        for j in range(len(napis)):
            if napis[j] != skrot[j % len(skrot)]:
                roznice = roznice+1
                if roznice > 1:
                    break

        if roznice <= 1:
            return len(skrot)

    return len(skrot)

a = int(input())
for i in range(0,a):
    b = int(input())
    x = input()
    z = sprawdzanie(x)
    print(z)




