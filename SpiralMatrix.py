# LeetCode 54: Spiral Matrix
from typing import List
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    m = len(matrix)
    n = len(matrix[0])
    ans = []
    for i in range((min(m,n)+1)//2):
        # 1. iterate over ith row
        for j in range(i,n-i):
            ans.append(matrix[i][j])
        #  2. iterate over (n-i)th col
        for k in range(i+1,m-i):
            ans.append(matrix[k][n-i-1])
        #  3. iterate over (n-i)th row in reverse order
        if m-i-1 > i:
            for j in range(n-2-i,i-1,-1):
                ans.append(matrix[m-i-1][j])
        #  4. iterate over ith col in reverse order
        if n-1-i > i:
            for k in range(m-2-i,i,-1):
              ans.append(matrix[k][i])
    return ans
#  approach 2
def spiralOrder_(matrix: List[List[int]]) -> List[int]:
    ans = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    while left < right and top < bottom:
        for j in range(left, right):
            ans.append(matrix[top][j])
        top += 1

        for i in range(top, bottom):
            ans.append(matrix[i][right-1])
        right -= 1

        if not (left < right and top < bottom):
            break
        
        for j in range(right-1,left-1,-1): 
            ans.append(matrix[bottom-1][j])
        bottom -= 1

        for i in range(bottom-1,top-1,-1):
            ans.append(matrix[i][left])
        left += 1
    return ans

def print_matrix(matrix):
    for row in matrix:
        print(row)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print_matrix(matrix)
print("Spiral order:",spiralOrder(matrix))
print("Spiral order_:",spiralOrder_(matrix))
print()

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print_matrix(matrix)
print("Spiral Order:",spiralOrder(matrix))
print("Spiral Order_:",spiralOrder_(matrix))
print()

matrix = [[2,5,8],[4,0,-1]]
print_matrix(matrix)
print("Spiral Order:",spiralOrder(matrix))
print("Spiral Order_:",spiralOrder_(matrix))