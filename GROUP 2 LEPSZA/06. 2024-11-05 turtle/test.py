n = int(input())
p = 1
c = 0
if n>=6:
    for i in range(n//6+1):
        #print(p)
        for j in range(1,6+1):
            if j!=1 and  c == 1:
                if j%2==0:
                    p = p+3
                else:
                    p = p-1
                c = c+1
        if i%2==0:
            p = p-10
    print(p)
else:
    for j in range(1,n+1):
        if j!=1:
            if j%2==0:
                p = p+3
            else:
                p = p-1
    print(p)