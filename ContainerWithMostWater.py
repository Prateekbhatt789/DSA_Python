# Leetcode 11 container with most water
from typing import List
def maxArea(height: List[int]) -> int:
        l,r = 0, len(height)-1
        maxArea =0
        while(l<r):
            min_height = min(height[l],height[r])
            maxArea= max(maxArea,(r-l)*min_height)
            if min_height == height[l]:
                l+=1
            else:
                r-=1
        return maxArea

nums = [1,8,6,2,5,4,8,3,7]
print(maxArea(nums))