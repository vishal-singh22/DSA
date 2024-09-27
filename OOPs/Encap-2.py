#Create a class Student that encapsulates the details of a student (name, age, marks) and provides methods to set and get the marks. 
# Ensure that marks can only be set through a method.

class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.__marks = None
    
    def set_marks(self,marks):
        if 0 <= marks <=100:
            self.__marks = marks
            print(f"\nmarks for {self.name} have been set that is {self.__marks}")
        else:
            print("\nenter marks must be in lie in 0 to 100")
            
    def get_marks(self):
        if self.__marks is not None:
            return f"\n{self.name} marks is {self.__marks}"
        else:
            return f"\nmarks for {self.name} is not set yet"
        
    def get_details(self):
        print(f"\nStudent Details:\nName: {self.name}\nAge: {self.age}")
        print(self.get_marks()) 
        
        
if __name__ == "__main__":
    std1 = Student("vishal",19)
    std2 = Student("yuvraj",18)
    
    std1.get_details()
    
    std1.set_marks(85)
    
    std1.get_details()
    
    std2.get_details()
    
    std2.set_marks(98)
    
    std2.get_details()
    