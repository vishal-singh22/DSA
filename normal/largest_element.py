"""we check the largest element in the aray
   input arr = [1,5,2,3,0]
   output 5

   Explaination = 5 is the largest number in the array"""

def largest(arr):
    max = arr[0]
    n = len(arr)
    for i in range(n):
        if max < arr[i]:
            max = arr[i]
    return max

arr = [2,5,1,3,0]
print(largest(arr),"is the largest element in the array")

#Approach 2 brute method

def largest2(arr):
    arr.sort()
    n = len(arr)
    return arr[n-1]

print(largest(arr),"is the largest element in the array")



   
