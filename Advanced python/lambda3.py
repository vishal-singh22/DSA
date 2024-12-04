numbers = [5, 10, 15, 20, 25]
result = list(map(lambda x: x * 2, filter(lambda x: x % 10 == 0, numbers)))
print(result)
