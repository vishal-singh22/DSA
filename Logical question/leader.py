"""
iven an array, print all the elements which are leaders.
A Leader is an element that is greater than all of the elements on its right side in the array.
Input:

 arr = [10, 22, 12, 3, 0, 6]
Output:

 22 12 6
Explanation:

 6 is a leader.
 In addition to that, 12 is greater than all the elements in its right side (3, 0, 6),
 also 22 is greater than 12, 3, 0, 6.
"""

def find_leaders(arr,n):
    leaders = []
    
    for i in range(n):
        is_leader = True
     
        for j in range(i+1,n):
            if arr[i] <  arr[j]:
                is_leader = False
                break
            
        if is_leader:
            leaders.append(arr[i])
    
    return leaders
            

# optimal approach in O(n) time

def printLeaders(arr, n):
    ans = []
  
    # Last element of an array is always a leader,
    # push into ans array.
    max_elem = arr[n - 1]
    ans.append(arr[n - 1])

    # Start checking from the end whether a number is greater
    # than max no. from right, hence leader.
    for i in range(n - 2, -1, -1):
        if arr[i] > max_elem:
            ans.append(arr[i])
            max_elem = arr[i]

    return ans[::-1]

arr = [10, 22, 12, 3, 0, 6]   
n = len(arr)
print(find_leaders(arr,n))  

print(printLeaders(arr,n)) 