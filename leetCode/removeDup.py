nums = [2, 3, 3, 4, 3, 6, 6, 7, 7, 8, 2, 9]

def remove_dup(list):
    good_list = []
    bad_list = []
    for i in range(len(list)):
        if good_list.__contains__(list[i]):
            bad_list.append(list[i])
        else:
            good_list.append(list[i])

    return good_list

def remove_same(list):
    new_list = set(list)
    return new_list

print(remove_same(nums))