class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def add(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
        
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev     
               
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next
            
if __name__ == "__main__":
    
    Llist = Linkedlist()
    Llist.add(12)
    Llist.add(1)
    Llist.add(2)
    Llist.add(17)
    Llist.add(10)
    Llist.add(8)
    
    print("\n\nbefore reverse the list")
    Llist.display()
    
    Llist.reverse()
    print("\n\nafter reverse the list")
    
    Llist.display()
            
        
        
        
            

        
    
        