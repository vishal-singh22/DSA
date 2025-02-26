import numpy as np

A = np.array([
       [1,3,5],
       [5,8,9],
       [2,4,8]
    ])

B = np.array([
       [5,3,2],
       [1,6,9],
       [3,4,7]
    ])
#find the matrix multiplication
print(np.dot(A,B),"\n")
print(A@B,"\n")
print(A.dot(B),"\n")
print(np.matmul(A,B),"\n\n\n")


# find the inverese of the matrix

print(np.linalg.inv(A))
