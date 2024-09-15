def second_max(arr):
    n = len(arr)
    
    if n < 2:
        return -1
    first_largest = float('-inf')
    second_largest = float('-inf')
    for i in range(1,n):
        
        if arr[i] > first_largest:
            second_largest = first_largest
            first_largest = arr[i]
            
        elif arr[i] > second_largest and arr[i]!= first_largest:
            second_largest = arr[i]
            
    return second_largest

def second_min(arr):
    n = len(arr)
    if n<2:
        return -1
    first_smaller = float('inf')
    second_smaller = float('inf')
    
    for i in range(1,n):
        if arr[i] < first_smaller:
            second_smaller = first_smaller
            first_smaller = arr[i]
        elif arr[i]< second_smaller and arr[i]!= first_smaller:
            second_smaller = arr[i]


    return second_smaller
        
arr =[1, 2, 4, 7, 5]

print("econd largest element is:",second_max(arr))
print("second smallest element is:",second_min(arr))

arr = [-5, -1, -9, -3]
print("econd largest element is:",second_max(arr))
print("second smallest element is:",second_min(arr))

arr = [5]
print("econd largest element is:",second_max(arr))
print("second smallest element is:",second_min(arr))


