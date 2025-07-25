# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def remove_val(nums: list[int], val: int) -> int:
    # i = 0
    # j = len(nums) - 1

    # while i <= j:
    #     if nums[i] == val and nums[j] == val:
    #         j -= 1
    #     elif nums[i] == val and nums[j] != val:
    #         nums[i] = nums[j]
    #         i += 1
    #         j -= 1
    #     else:
    #         i += 1

    # return i, nums

    k = 0
        
    for i in range(len(nums)):
        if nums [i] != val:
            print(nums[k], nums[i])
            nums[k] = nums[i]
            k += 1
    return k, nums

print(remove_val([0,1,2,2,3,0,4,2], 2))
print(remove_val([1], 1))