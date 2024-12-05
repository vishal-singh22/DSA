from functools import reduce

# Input list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Filter even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Step 2: Map the even numbers to their squares
squared_even_numbers = map(lambda x: x ** 2, even_numbers)

# Step 3: Reduce to find the sum of squared even numbers
sum_of_squares = reduce(lambda x, y: x + y, squared_even_numbers)

# Output the result
print(f"Sum of squares of even numbers: {sum_of_squares}")
