def find_missing_number(list):
    list_length = max(list)
    list_sum = sum(list)
    expected_sum = (list_length * (list_length + 1)) // 2

    return expected_sum - list_sum


print(find_missing_number([1, 2, 3, 4, 6]))