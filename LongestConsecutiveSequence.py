# LeetCode 128 Longest Consecutive Sequence
from typing import List
def longestConsecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    max_len =0
    for num in nums_set:
        if num-1 not in nums_set:
            length =1
            while num+length in nums_set:
                length += 1
            max_len = max(max_len,length)
    return max_len

print(longestConsecutive([100,1,200,4,3,2]))