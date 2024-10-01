"""Input:
 [[1,2,3],[4,5,6],[7,8,9]]

Output
: [[7,4,1],[8,5,2],[9,6,3]]

Explanation:
 Rotate the matrix simply by 90 degree clockwise and return the matrix.
"""

def rotate(matrix: list[list[int]]) -> None:
    
    n = len(matrix)
    
    for i in range(n):
        for j in range(i):
            matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

    
    for i in range(n):
        matrix[i].reverse()

if __name__ == "__main__":
    
    arr = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]  
    
    rotate(arr)
    
    print("rotate array is :")
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j],end ='')
        print()
            
    