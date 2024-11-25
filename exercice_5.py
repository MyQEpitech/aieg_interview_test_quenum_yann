def custom_sort(unsorted_list):
    sorted_list = sorted(unsorted_list, key=len)
    return sorted_list


print(custom_sort(["rohan", "amy", "sapna", "muhammad","aakash", "raunak", "chinmoy"]))