# nie dziala :(
# nie rozumiem to co ponizej liczy ale roznice maxymalna a nie sume podciagu.

#plan: podzielimy na 2 funkcje
# max_spadek - czyli analogicznie do wagi szukam gdzie wartosc spadla najbardziej "schudlem"
# max wzrost - czyli analogicznie do wagi tylko szukam gdzie wartosc przyrozla najbardziej "przytylem"

# max_spadek - czyli analogicznie do wagi szukam gdzie wartosc spadla najbardziej "schudlem"
def func_najwiekszy_spadek(lista_nums):
    if len(lista_nums)<=1:
        return 0

    max_napotkana_wartosc = lista_nums[0]
    max_spadek = 0

    for num in lista_nums[1:]: # zapis wagi[1:] bierze on [1..n-1] bo [0] mamy juz wykorzystany
        if num > max_napotkana_wartosc:
            max_napotkana_wartosc = num
        if (num - max_napotkana_wartosc) < max_spadek:
            max_spadek = (num - max_napotkana_wartosc)
    return max_spadek

# max wzrost - czyli analogicznie do wagi tylko szukam gdzie wartosc przyrozla najbardziej "przytylem"
def func_najwiekszy_wzrost(lista_nums):
    if len(lista_nums)<=1:
        return 0

    min_napotkana_wartosc = lista_nums[0]
    max_wzrost = 0

    for num in lista_nums[1:]: # zapis wagi[1:] bierze on [1..n-1] bo [0] mamy juz wykorzystany
        if num < min_napotkana_wartosc:
            min_napotkana_wartosc = num
        if (num - min_napotkana_wartosc) > max_wzrost:
            max_wzrost = (num - min_napotkana_wartosc)
    return max_wzrost

def max_abs_subarray_sum(lista_nums):
    najwiekszy_spadek = func_najwiekszy_spadek(lista_nums)
    najwiekszy_wzrost = func_najwiekszy_wzrost(lista_nums)
    max_abs_subarray_sum_ret = max(abs(najwiekszy_spadek), abs(najwiekszy_wzrost))
    print(f"{lista_nums} => {najwiekszy_spadek=} {najwiekszy_wzrost=} => {max_abs_subarray_sum_ret}")

    return max_abs_subarray_sum_ret

# funkcja ktora laczy  func_najwiekszy_spadek() oraz func_najwiekszy_wzrost()
def max_abs_subarray_sum_merged(lista_nums):
    if len(lista_nums)<=1:
        return 0

    max_napotkana_wartosc = lista_nums[0]
    max_spadek = 0

    min_napotkana_wartosc = lista_nums[0]
    max_wzrost = 0


    for num in lista_nums[1:]: # zapis wagi[1:] bierze on [1..n-1] bo [0] mamy juz wykorzystany
        if num > max_napotkana_wartosc:
            max_napotkana_wartosc = num
        if (num - max_napotkana_wartosc) < max_spadek:
            max_spadek = (num - max_napotkana_wartosc)

        if num < min_napotkana_wartosc:
            min_napotkana_wartosc = num
        if (num - min_napotkana_wartosc) > max_wzrost:
            max_wzrost = (num - min_napotkana_wartosc)

    max_abs_subarray_sum_ret = max(abs(max_spadek), abs(max_wzrost))
    print(f"{lista_nums} => {max_spadek=} {max_wzrost=} => {max_abs_subarray_sum_ret}")
    return max_abs_subarray_sum_ret

def max_abs_subarray_sum_refactor(lista_nums):
    if len(lista_nums)<=1:
        return 0

    min_napotkana_wartosc = max_napotkana_wartosc = lista_nums[0]
    max_spadek = max_wzrost = 0

    for num in lista_nums[1:]: # zapis wagi[1:] bierze on [1..n-1] bo [0] mamy juz wykorzystany
        max_napotkana_wartosc = max(max_napotkana_wartosc, num)
        max_spadek            = min(max_spadek, (num - max_napotkana_wartosc))
        min_napotkana_wartosc = min(min_napotkana_wartosc, num)
        max_wzrost            = max(max_wzrost,(num - min_napotkana_wartosc) )

    max_abs_subarray_sum_ret = max(abs(max_spadek), abs(max_wzrost))
    print(f"{lista_nums} => {max_spadek=} {max_wzrost=} => {max_abs_subarray_sum_ret}")
    return max_abs_subarray_sum_ret





print("# Przykłady: max_abs_subarray_sum")
lista_nums1 = [1, -3, 2, 3, -4]
print(f"{lista_nums1} {max_abs_subarray_sum(lista_nums1)=}")

lista_nums1 = [2, -5, 1, -4, 3, -2]
print(f"{lista_nums1} {max_abs_subarray_sum(lista_nums1)=}")


print("# Przykłady: max_abs_subarray_sum_merged")
max_abs_subarray_sum_merged([1, -3, 2, 3, -4])
max_abs_subarray_sum_merged([2, -5, 1, -4, 3, -2])

print("# Przykłady: max_abs_subarray_sum_merged")
max_abs_subarray_sum_refactor([1, -3, 2, 3, -4])
max_abs_subarray_sum_refactor([2, -5, 1, -4, 3, -2])
max_abs_subarray_sum_refactor([0, 2, 2])
max_abs_subarray_sum_refactor([0, -2, -2, -1])
