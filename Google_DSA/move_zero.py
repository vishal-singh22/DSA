# all zero put at last of the array  and and non negative number put on front of the array


def move_zero(arr):
    arr1 = []
    count = 0

    for i in arr:
        if i is not 0 :
            arr1.append(i)
        else:
            count += 1

    for i in range(count):
        arr1.append(0)
        
    return arr1

   
arr =[ 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]

print(move_zero(arr))
