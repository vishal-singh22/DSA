def Linear_search(arr,target):
    n = len(arr)

    for i in range(1,n):
        if arr[i] == target:
            return i

arr = [1, 2, 3, 4, 5]

target = 3

print(f"{target} at {Linear_search(arr,target)} index postion")
