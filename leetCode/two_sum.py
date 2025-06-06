# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]

def two_sum(arr, target):
    seen_nums = {}

    for i, n in enumerate(arr):
        diff = target - n
        if diff in seen_nums:
            return [seen_nums[diff], i]
        seen_nums[n] = i

print(two_sum([3,4,5,6], 7))