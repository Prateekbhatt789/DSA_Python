# Leetcode 167: Two SumII -Input Array is Sorted

def twoSum(numbers: list[int], target: int) -> list[int]:
        i,j= 0,len(numbers)-1
        while i<j:
            sum = numbers[i]+numbers[j]
            if sum == target:
                return [i+1,j+1]
            elif sum > target:
                j-=1
            else:
                i+=1
        return []

print(twoSum([2,3,7,11,15],9))