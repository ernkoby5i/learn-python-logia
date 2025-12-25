slowo = "ogrodzenie"

def sprawdzam(slowo):
    sam = ['a', 'e', 'i', 'o', 'u', 'y']
    s_sam = {}
    s_spo = {}
    for i in slowo:
        if i in sam:
            if i in s_sam:
                s_sam[i] = s_sam[i] + 1
            else:
                s_sam[i] = 1
        else:
            if i in s_spo:
                s_spo[i] = s_spo[i] + 1
            else:
                s_spo[i] = 1
    return s_spo,s_sam

n = int(input())
slowa = []
for i in range(0,n):
    slowo = input()
    slowa.append(slowo)
for i in slowa:
    s_spo,s_sam = sprawdzam(i)

    for i in sorted(s_sam):
        print(i,end="")
        if s_sam[i] != 1:
            print(s_sam[i],end='')

    for i in sorted(s_spo):
        print(i,end="")
        if s_spo[i]!=1:
            print(s_spo[i],end='')
    print("")
