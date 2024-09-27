# Create a class Car with attributes like model, year, and color.
# Write methods to display car details and start the engine.

class car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
    
    def show(self):
         print(f"Car Details:\nModel: {self.model}\nYear: {self.year}\nColor: {self.color}")
         
if __name__ == "__main__":
    
    a = car('bmw',2020, "royal black")
    b= car("oddi",2013,"prime red")
    a.show()
