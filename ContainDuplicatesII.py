# Leetcode 219 contain Duplicates
def containDuplicatesII(nums,k):
    num_map = {}  # key is nums[i] and value is last occurance of nums[i] in num_map
    for i,num in enumerate(nums):
        if num in num_map:
            j = num_map[num]
            if abs(j-i) <= k:
                return True
        num_map[num] = i
    return False

print(containDuplicatesII([1,2,3,1],3))
print(containDuplicatesII([1,2,3,1],2))
print(containDuplicatesII([1,2,3,1,2,3], 2))