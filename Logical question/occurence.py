# from collections import Counter

# bucket = ["eggs","bread","Milk","bread", "banana","Milk","bread","banana","eggs","eggs"]

# bucket_item = Counter(bucket)

# print(bucket_item)


bucket = ["eggs","bread","Milk","bread", "banana","Milk","bread","banana","eggs","eggs"]

new_bucket = {}

for item in bucket:
    if item in new_bucket:
        new_bucket[item] +=1
        
    else:
        new_bucket[item] = 1
        
print(new_bucket)

