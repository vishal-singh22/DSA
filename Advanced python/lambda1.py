# Sorting a list of dictionaries by a specific key
data = [{'name':"vasu","age":21},{"name":"vishal","age":18},{'name':"singh","age":22},{"name":"yuvi","age":19}]
sorted_data = sorted(data,key = lambda x: x['age'])
print(sorted_data)