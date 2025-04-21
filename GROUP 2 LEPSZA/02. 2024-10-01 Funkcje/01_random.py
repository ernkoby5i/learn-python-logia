from random import randint

def funkcja():
    wynik = ""
    for i in range(10):
        wynik += chr(randint(97,2000))
    print(wynik)

for i in range(5):
    funkcja()

x = max(1,3) # max returnuje 3
x *= 2
print(x)