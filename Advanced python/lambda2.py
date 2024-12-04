def power_of(exp):
    return lambda x: x ** exp

square = power_of(2)
cube = power_of(3)

print(square(5))
print(cube(2))