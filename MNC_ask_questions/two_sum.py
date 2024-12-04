def two_sum(list,target):
    l=[]
    n = len(list)
    for i in range(n):
        for j in range(i+1,n):  
            if(list[i] + list[j] == target):
                l.append(i)
                l.append(j)
                return l
    return None

l=[2,7,11,15]
target = 13
print(two_sum(l,target))
                
            
