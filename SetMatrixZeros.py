# Leetcode 73: Set Matrix Zeros
from typing import List
def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    zero_row = set()
    zero_col = set()
    m,n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_row.add(i)
                zero_col.add(j)
    if len(zero_row) == 0 and len(zero_col) == 0:
        return
    for i in range(m):
        for j in range(n):
            if i in zero_row or j in zero_col:
                matrix[i][j]=0
    # # Row handling
    # for row in zero_row:
    #     for j in range(n):
    #         matrix[row][j] = 0
    # # Col handling
    # for col in zero_col:
    #     for j in range(m):
    #         matrix[j][col] = 0
    

def print_matrix(matrix):
    for row in matrix:
        print(row)

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print_matrix(matrix)
setZeroes(matrix)
print_matrix(matrix)
print()

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print_matrix(matrix)
setZeroes(matrix)
print_matrix(matrix)