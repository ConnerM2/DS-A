# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def majority_element(nums: list[int]) -> int:
    my_dict = {}
    majority = len(nums) / 2

    for num in nums:
        if num in my_dict:
            my_dict[num] += 1
        else:
            my_dict[num] = 1

        if my_dict[num] >= majority:
            return num

    return my_dict


print(majority_element([2,2,1,1,1,2,2]))