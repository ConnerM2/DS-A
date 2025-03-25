# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    
    midx = m - 1
    nidx = n - 1
    ridx = m + n - 1

    while nidx >= 0:
        if midx >= 0 and nums1[midx] > nums2[nidx]:
            nums1[ridx] = nums1[midx]
            midx -= 1
        else:
            nums1[ridx] = nums2[nidx]
            nidx -= 1

        ridx -= 1
    print(nums1)

merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
