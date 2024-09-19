def find_value_in_ones(arr):
    xorr = 0

    for i in arr:
        xorr ^= i
        
    return xorr

arr= [4,1,2,1,2]

print(find_value_in_ones(arr))


''' Example 2:
Input Format:
 arr[] = {4,1,2,1,2}
Result:
 4
Explanation:
 In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.
'''
