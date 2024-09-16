def rotate_array(arr,k):
    k = k% len(arr)
    arr[:]= arr[-k:] + arr[:-k]
    return arr

arr = [1,2,3,4,5,6,7]

n = int(input("enter the value for rotate: "))
print(rotate_array(arr,n))
