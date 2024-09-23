"""Example 1:
Input Format:
 N = 3, M = 4, target = 8,
mat[] = 
1 2 3 4
5 6 7 8 
9 10 11 12
Result:
 true
Explanation:
 The ‘target’  = 8 exists in the 'mat' at index (1, 3)."""
 
def search_Matrix(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                return True
           
    return False


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
target = 89
result = search_Matrix(matrix, target)
print(f"{target} in matrix" if result else f"{target} is not in matrix")
    
    
                