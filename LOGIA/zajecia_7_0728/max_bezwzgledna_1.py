# nie dziala :(
# nie rozumiem

def max_abs_subarray_sum(nums):
    if len(nums)<1:
        return 0

    max_sum = curr_dodatani = nums[0]
    min_sum = curr_ujemny = nums[0]

    for num in nums[1:]:
        if curr_dodatani + num > curr_dodatani:
            curr_dodatani = curr_dodatani + num
        else:
            curr_dodatani = num

        if max_sum<curr_dodatani:
            max_sum = curr_dodatani

        curr_ujemny = min(num, curr_ujemny + num)
        if curr_ujemny < curr_ujemny + num:
            curr_ujemny = curr_ujemny + num
        else:
            curr_ujemny = num


        if min_sum<curr_ujemny:
            min_sum = curr_ujemny


    return max(abs(max_sum), abs(min_sum))

# Przykłady:
lista_nums = [1, -3, 2, 3, -4]
print(f"{lista_nums} {max_abs_subarray_sum(lista_nums)}")

lista_nums = [2, -5, 1, -4, 3, -2]
print(f"{lista_nums} {max_abs_subarray_sum(lista_nums)}")
