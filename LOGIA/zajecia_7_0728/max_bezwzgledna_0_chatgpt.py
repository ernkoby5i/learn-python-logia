def max_abs_subarray_sum(nums):
    max_sum = curr_max = nums[0]
    min_sum = curr_min = nums[0]

    for num in nums[1:]:
        curr_max = max(num, curr_max + num)
        max_sum = max(max_sum, curr_max)

        curr_min = min(num, curr_min + num)
        min_sum = min(min_sum, curr_min)

    return max(abs(max_sum), abs(min_sum))

# Przykłady:


lista_nums = [1, -3, 2, 3, -4]
print(f"{lista_nums} {max_abs_subarray_sum(lista_nums)}") # -> 5

lista_nums = [2, -5, 1, -4, 3, -2]
print(f"{lista_nums} {max_abs_subarray_sum(lista_nums)}") # -> 8
