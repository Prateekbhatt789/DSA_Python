# Leetcode: 15 3Sum

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums = sorted(nums)
    for i,num in enumerate(nums):
        if i>0 and nums[i]== nums[i-1]:
            continue
        duplet_list = twoSum(nums,-num,i+1)
        if duplet_list:
            for duplet in duplet_list:
                # duplet.insert(0,-num)
                triplet = [num] + duplet
                result.append(triplet)

    return result

def twoSum(nums: List[int],target: int,startIndex: int):
    j= len(nums)-1
    if startIndex >= j:
        # only 1 element or less
        return []
    duplets = []
    while startIndex < j:
        if nums[startIndex] + nums[j] < target:
            startIndex+=1
        elif nums[startIndex] + nums[j] > target:
            j-=1
        else:
            duplets.append([nums[startIndex],nums[j]])
            # updating startIndex and j also addressing duplicate entries
            while startIndex < j and nums[startIndex+1] == nums[startIndex]:
                startIndex+=1
            while startIndex < j and nums[j] == nums[j-1]:
                j-=1
            startIndex += 1
            j -= 1
    return duplets

def threeSumModified(nums: List[int]) -> List[List[int]]:
    nums.sort()
    triplet = set()
    n = len(nums)
    for i in range(n):
        first = nums[i]
        l = i+1
        r = n-1
        while l<r:
            currsum = first + nums[l] + nums[r]
            if currsum > 0:
                r -= 1
            elif currsum < 0:
                l += 1
            else:
                triplet.add((first, nums[l], nums[r]))
                l+=1
                r-=1
    return [list(t) for t in triplet]


# nums = [-1,0,1,2,-1,-4]
nums = [3,0,-2,-1,1,2]
print("triplet:",threeSum(nums))
print("triplet threesum modified:",threeSumModified(nums))
    