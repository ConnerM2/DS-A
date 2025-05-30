# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores)

def remove_dupII(nums: list[int]) -> int:
    k = 2

    for i in range(2, len(nums)):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1
    return k, nums

print(remove_dupII([0,0,1,1,1,1,2,3,3]))