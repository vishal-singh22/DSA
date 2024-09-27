#Create a parent class Animal with a method speak. 
#Inherit two child classes Dog and Cat, and override the speak method to print appropriate sounds.

class Animal:
    def speak(self):
        print("the animal makes a sound")
        

class Dog(Animal):
    def speak(self):
        print("The dog says: Woof!")
        

class Cat(Animal):
    def speak(self):
        print("the cat says: Meow!")
        
class Car(Animal):
    def speak(self):
        print("my car says: Wrom-Wrom!")

my_dog = Dog()

my_cat = Cat()

my_car = Car()

my_dog.speak()

my_cat.speak()

my_car.speak()
        
        
        