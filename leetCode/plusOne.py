nums = [2,4,1,6,2]
word = 'Hello'
target = 5

def sum_of_nums(nums, target=5):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]
            
print(sum_of_nums(nums))

