a = int(input())
b = int(input())
dni = 0
for i in range (0 ,a-1):
    if i <= 10:
        if i%2!=0:
            dni = dni + 11
        else:
            dni = dni + 13
    else:
        if i%2!=0:
            dni = dni + 13
        else:
            dni = dni + 11

dni = dni + b
print(dni)