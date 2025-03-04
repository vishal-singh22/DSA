''' daily target for crack tcs like company
1. array
2. number
3. number system
4. sorting
5. string'''

# array
def smallest(arr):
    arr.sort()
    return arr[0]
def largest(arr):
    arr.sort()
    return arr[-1]
def sec_small_large(arr):
    # first approach
    lar = 0
    small = arr[0]
    sec_lar = 0
    sec_small = arr[0]
    for i in arr:
        if i > lar:
            sec_lar = lar
            lar = i
        elif sec_lar!=0 and i > sec_lar:
            sec_lar = i
    print("second largest element",sec_lar)
    for i in arr:
        if i < small:
            sec_small = small
            small = i
        elif sec_small!=0 and i< sec_small:
            sec_small = i
    print("second smallest number ",sec_small)
    #second approach
    arr.sort()
    return arr[1],arr[-2]
arr = [2,5,1,3,0]
print(smallest(arr))
print(largest (arr))
print(sec_small_large(arr))   
