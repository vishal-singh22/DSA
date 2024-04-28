def kthFactor(k,n):
    count=0
    for i in range(1,n):
        if(n%i==0):
            count+=1
        if(count==k):
            return i
    return -1
n=int(input("enter the nth value : "))
k=int(input("enter the kth value : "))
res=kthFactor(k,n)
print(res)
