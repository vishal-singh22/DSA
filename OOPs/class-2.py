#Define a class Rectangle with methods to calculate the area and perimeter. 
#Create objects of this class to find the area and perimeter of different rectangles.

class rectangle:
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
        
    def area(self):
        print(f"area of rectangle is : {self.length * self.breath}")
        
    def parameter(self):
        print(f"parameter of the rectangel is : {2*(self.length + self.breath)}")
    
    
if __name__ == "__main__":
    
    rect = rectangle(4,5)
    rect.area()
    rect.parameter()