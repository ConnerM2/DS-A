arra1, arra2 = [0, 3, 4, 21], [4, 6, 30]
# should return 0, 3, 4, 4, 6, 21, 30
def merge_two_sorted_arr(arr1, arr2):
    i, j = 0, 0
    merged_arr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    merged_arr.extend(arr1[i:])
    merged_arr.extend(arr2[j:])

    return merged_arr

print(merge_two_sorted_arr(arra1, arra2))