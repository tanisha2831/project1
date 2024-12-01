class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 

class Stack:
    def __init__(self):
        self.top = None 
        
    def push(self, elt):
        new = Node(elt) 
        new.next = self.top
        self.top = new
        print(f"{elt} pushed")
        
    def pop(self):
        if self.top is None:  
            print("stack is empty")
        else:
            temp = self.top.data 
            self.top = self.top.next  
            print(f"\n{temp} popped\n")
            
    def display(self):
        current = self.top 
        while current:
            print(current.data) 
            current = current.next  


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.display()
s.pop()
s.display()
