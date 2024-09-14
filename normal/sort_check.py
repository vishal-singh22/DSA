def sort_check(arr):
    n = len(arr)
    flag =1
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return False
    return True
        


arr1 = [1,2,3,4,5]
arr2 = [5,4,6,7,8]

print(sort_check(arr1))
print(sort_check(arr2))
