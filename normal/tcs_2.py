def update_arr(arr):
    for i in range(len(arr)):
        if arr[i]==arr[i-1]:
            arr[i-1] = arr[i-1]*2
            arr[i] = 0
    j = 0
    for k in range(len(arr)):
        if arr[k]!=0:
            arr[k],arr[j]=arr[j],arr[k]
            j+=1
    return arr

arr = [1,2,2,1,1,0]
print(update_arr(arr))


# zero at the end of the arr

def shift_zero(arr):
    j = 0
    for k in range(len(arr)):
        if arr[k]!=0:
            arr[k],arr[j]=arr[j],arr[k]
            j+=1
    return arr

arr = [1,4,0,2,0,0]

print(shift_zero(arr))
    
