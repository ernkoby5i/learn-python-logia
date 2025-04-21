n = int(input())
l2 = list(map(int, input().split()))



if n%2==0:
    x = -1
    d = 0
    for i in range (0, n//2):
        #print(i)
        print(l2[d],end=" ")
        print(l2[x],end=" ")
        x = x - 1
        d = d+1
else:
    x = -1
    d = 0
    print(l2[d], end=" ")
    d = d+1
    for i in range (0, n//2):
        #print(i)
        print(l2[x], end=" ")
        print(l2[d],end=" ")
        x = x - 1
        d = d+1

