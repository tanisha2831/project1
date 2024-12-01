class Stack:
    def __init__(self,sz):
        self.top=-1
        self.size=sz
        self.data=[]
        for i in range(sz):
            self.data.append(0)
            
    def push(self,elt):
        if self.top==self.size-1:
            print("stack is full")
        else:
            self.top+=1
            self.data[self.top]=elt
            print(f"{elt} pushed")
            
    def pop(self):
        if self.top==-1:
            print("stack is empty")
        else:
            temp=self.data[self.top]
            self.top-=1
            print(f"\n{temp} popped\n")
            
    def display(self):
        t=self.top
        while t>=0:
            print(self.data[t])
            t=t-1
        
s=Stack(3)
s.push(1)
s.push(2)
s.push(3)
s.display()
s.pop()
s.display()
