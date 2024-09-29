class stack:
    
    def __init__(self):  
        self.stack = []
      
        
    def is_empty(self):  
        return len(self.stack) == 0
    
    def push(self ,items):
        self.stack.append(items)
        print(f"pushed: {items}")
        
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack.pop()
    
    def display(self):
        print("stack ",self.stack)
        
        
if __name__ == "__main__":
    stk = stack()
    
    stk.push(15)
    stk.push(5)
    stk.push(1)
    stk.push(12)
    stk.push(16)
    stk.push(0)
    stk.display()
    
    print("Popped:", stk.pop())  
    stk.display()
    
    