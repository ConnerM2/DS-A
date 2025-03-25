# 2-pointer that sums the left and right
# If sum is smaller than goal, move left pointer up
# If sum is bigger than goal, move right pointer down
# This will be O(N)
def get_sum(array, sum):
    i = 0
    j = len(array) - 1

    for num in range(len(array)):
        print(f"loop num: {num}")
        print(i, j)
        print(array[i]+array[j])

        if len(array) <= 1:
            return False
        if i == j:
            return False
        elif array[i] + array[j] < sum:
            i += 1
        elif array[i] + array[j] > sum:
            j -= 1
        elif array[i] + array[j] == sum:
            return True

print(get_sum([1, 2, 3, 4], 0))  # Expected: False

# This allows the array to not be sorted
# Add the total - item into a set
# loop through array
# If there is match, there must be a pair that add to total
def get_sum2 (arr, total):
    new_set = set()
    for item in arr:
        if item in new_set:
            return True
        new_set.add(total - item)
        print(new_set)
    return False

print(f"get_sum2 {get_sum2([6,4,3,2,1,7], 9)}")

# <---------------------------------->
# Given 2 arrays find if there is match
# array1 = ["a", "b", "c"]
# array2 = ["c", "x"] return True

# parameters (arr1, arr2)
# return True or False

# brute force (O(a * b)
# def brute_force(arr1, arr2):
#     for item1 in arr1:
#         for item2 in arr2:
#             if item1 == item2:
#                 return True
#     return False

def is_match(arr1, arr2):
    default_val = True
    dictionary = dict.fromkeys(arr1, default_val)
    for item in arr2:
        if item in dictionary:
            return True
    return False

print(is_match(["a", "b", "c"], ["c", "x"])) # O(a + b)



