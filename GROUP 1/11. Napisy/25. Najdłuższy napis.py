n = int(input())
wysoka = None
poprzedni_len = 0

for i in range(0, n):
    s1 = list(input())
    x = len(s1)
    if x>poprzedni_len:
        print('JESEMMM TUUUUTAJJ!!!!')
        wysoka = s1
        poprzedni_len = x

for i in wysoka:
    print(i,end='')