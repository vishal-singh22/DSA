def max_consecutive_ones(arr):
    n = len(arr)
    count = 0
    max_count =0
    for i in range (n):
        if arr[i] == 1:
            count +=1
        else:
            count =0

        max_count = max(count,max_count)
    return max_count


arr = [1, 0, 1, 1, 0, 1]

print(max_consecutive_ones(arr))
