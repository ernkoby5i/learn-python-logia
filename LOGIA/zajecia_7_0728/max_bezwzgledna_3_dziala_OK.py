def najwiekszy_podciag(nums):
    max_positive_sum = curr_positive_sum = nums[0]

    for num in nums[1:]:
        curr_positive_sum = curr_positive_sum + num # dodajemy i zobaczymy
        if curr_positive_sum < 0:
            curr_positive_sum = 0 # reset bo lepiej porzucic to co mamy i wziac to co jest.

        max_positive_sum = max(max_positive_sum, curr_positive_sum) # suma liczb jest najbardziej dodatnia najwieksza powyzej 0

    print(f"{nums} => {max_positive_sum=}")

    return max_positive_sum


def najwiekszy_ujemny_podciag(nums):
    max_negative_sum = curr_negative_sum = nums[0]

    for num in nums[1:]:
        curr_negative_sum = curr_negative_sum + num # dodajemy nastepna liczbe.
        if curr_negative_sum > 0:
            curr_negative_sum = 0 # reset bo lepiej porzucic to co mamy i wziac to co jest.

        # i patrzymy czy akualny caig jest mniejszy
        max_negative_sum = max(max_negative_sum, curr_negative_sum) # suma liczb jest najbardziej dodatnia najwieksza powyzej 0

    print(f"{nums} => {max_negative_sum=}")

    return max_negative_sum


def max_abs_subarray_sum_proste(nums):
    max_positive_sum = curr_positive_sum = nums[0]
    max_negative_sum = curr_negative_sum = nums[0]

    for num in nums[1:]:

        # curr_max = max(num, curr_max + num)
        curr_positive_sum = curr_positive_sum + num # dodajemy i zobaczymy
        if curr_positive_sum < 0:
            curr_positive_sum = 0 # reset bo lepiej porzucic to co mamy i wziac to co jest.

        max_positive_sum = max(max_positive_sum, curr_positive_sum) # suma liczb jest najbardziej dodatnia najwieksza powyzej 0

        # curr_min = min(num, curr_min + num)
        curr_negative_sum = curr_negative_sum + num
        if curr_negative_sum > 0:   # chyba curr_negative_sum > 0 wiec po dodaniu liczby -1 lepiej porzucic curr_min i wziac samo -1
            curr_negative_sum = 0

        max_negative_sum = min(max_negative_sum, curr_negative_sum)
        if curr_negative_sum < max_negative_sum:
            max_negative_sum = curr_negative_sum # ten ciag jest najwiekszy ponizej 0

    iRet = max(abs(max_positive_sum), abs(max_negative_sum))
    print(f"{nums} {max_negative_sum=} {max_positive_sum=} => {iRet}")

    return iRet


print("# Przykłady: najwiekszy_podciag")
najwiekszy_podciag([1, -3, 2, 3, -4])
najwiekszy_podciag([2, -5, 1, -4, 3, -2])
najwiekszy_podciag([0, 2, 2])
najwiekszy_podciag([0, -2, -2, -1])


print("# Przykłady: max_abs_subarray_sum_proste")
max_abs_subarray_sum_proste([1, -3, 2, 3, -4])
max_abs_subarray_sum_proste([2, -5, 1, -4, 3, -2])
max_abs_subarray_sum_proste([0, 2, 2])
max_abs_subarray_sum_proste([0, -2, -2, -1])
max_abs_subarray_sum_proste([-3, -2, -2, -1])
