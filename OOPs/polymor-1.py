#Implement method overloading in Python (you can simulate it using default arguments or function name reuse) 
# to create a Calculator class with methods to add two, three, or four numbers.


class Calculator:

    def add(self, a, b, c=0, d=0):
        return a + b + c + d

class Calculator2:
    # Method to add any number of arguments using *args
    def add(self, *args):
        return sum(args)



if __name__ == "__main__":
    calc = Calculator()
    
    calc2 = Calculator2()

    # Add two numbers
    print(f"Adding two numbers (5 + 10): {calc.add(5, 10)}")

    # Add three numbers
    print(f"Adding three numbers (5 + 10 + 15): {calc.add(5, 10, 15)}")

    # Add four numbers
    print(f"Adding four numbers (5 + 10 + 15 + 20): {calc.add(5, 10, 15, 20)}")
    

    # Add two numbers
    print(f"Adding two numbers (5 + 10): {calc2.add(5, 10)}")

    # Add three numbers
    print(f"Adding three numbers (5 + 10 + 15): {calc2.add(5, 10, 15)}")

    # Add four numbers
    print(f"Adding four numbers (5 + 10 + 15 + 20): {calc2.add(5, 10, 15, 20)}")
