# Leetcode 209 Minimum size subarray sum
from typing import List
'''
The time complexity of this function is O(n) as we are performing insertion and deletion operation on each element of list into window
atmost one time only hence time complexity = O(2n) ~O(n)
'''
def minSubArrayLen(target: int, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        i = 0
        wlen = 10**5
        wsum = 0
        for j in range(n):
             wsum += nums[j]
             while wsum >= target:
                  wlen = min(wlen , j-i+1)
                  wsum -= nums[i]
                  i += 1
        return wlen if wlen != float('inf') else 0

print(minSubArrayLen(7, [2,3,1,2,4,3]))
print(minSubArrayLen(8, [3,2,1,2,1,3]))
