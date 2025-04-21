def czy_parzysta(n):
    if n % 2 == 0:
        return True
    else:
        return False

def czy_parzysta2(n):
    return n % 2 == 0

for i in range(10):
    if czy_parzysta(i):
        print(i, "jest parzyste/a")

        