# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]\

# Solution 1
# O(n) time complexity; O(n) space complexity
def rotate_array(nums: list[int], k: int) -> list[int]:
    new_arr = [0] * len(nums)
      # 9 % 7 = 2; This gives you shift amount even if it exceed the len(nums)
    k = k % len(nums)

    for i in range(len(nums)):
                # here, same idea, (6 + 2) % 7 = 1; This will wrap around the array
        new_arr[(i + k) % len(nums)] = nums[i]

    for i in range(len(nums)):
        nums[i] = new_arr[i]
    
    return nums

print(rotate_array([1,2,3,4,5,6,7], 3))