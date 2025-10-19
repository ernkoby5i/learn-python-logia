lista_operacji= [
    ['DOSTAWA','marchewka',10],
    ['ZAMOWIENIE', 'marchewka',3],
    ['ZAMOWIENIE', 'cebula', 4],
    ['DOSTAWA', 'marchewka', 1],
    ['ZAMOWIENIE', 'marchewka', 9],
]

stock = dict()

def magazyn(operacja,produkt,qty):
    print(f"{operacja},{produkt},{qty}")
    if operacja == 'DOSTAWA':
        stock[produkt] = stock.get(produkt,0) + qty

    elif operacja == "ZAMOWIENIE":
        ilosc_w_magazynie = stock.get(produkt,0)
        if ilosc_w_magazynie >= qty:
            stock[produkt] = ilosc_w_magazynie - qty
            print(f"TAK")
        else:
            print(f"NIE")

    else:
        print(f"{operacja} nieznanan")

    print(f"w magazynie po operacji {produkt}:{stock.get(produkt,0)}")
    return

print(stock)

for element_listy in lista_operacji:
    (operacja, produkt, qty) = element_listy
    magazyn(operacja, produkt, qty)

print(stock)
