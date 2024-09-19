"""
Example 1:
Input Format:
 N = 5, array[] = {1,2,4,5}
Result:
 3
Explanation: 
In the given array, number 3 is missing. So, 3 is the answer.

"""

def missing_value(arr,n):

    S1 = (n*(n+1))/2

    S2 =0

    for i in arr:  
        S2 += i
        
    return int(S1 - S2)

arr = [1,2,4,5]
n = 5

print(missing_value(arr,n))
    
