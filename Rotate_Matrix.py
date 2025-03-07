# Leetcode 48 Rotate Matrix by 90 clockwise
from typing import List
def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # 1. Transpose matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i+1):
            if i == j:
                continue
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    # 2. reverse list
    for i in range(n):
        matrix[i].reverse()
    
def printMatrix(matrix):
    for row in matrix:
        print(row)

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print("input:")
printMatrix(matrix)
rotate(matrix)
print("output")
printMatrix(matrix)