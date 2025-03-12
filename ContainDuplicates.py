# Leetcode 217: Contain Duplicates
def containDuplicates(nums):
    return not len(nums) == len(set(nums))

print(containDuplicates([1,2,3,1]))
print(containDuplicates([1,2,3,5]))