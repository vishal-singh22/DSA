def union(arr1,arr2):

    s = set()

    union = []

    for i in arr1:
        s.add(i)

    for i in arr2:
        s.add(i)

    return list(s)


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

print(union(arr1,arr2))
