class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue:
    def __init__(self,data):
        self.front=None
        self.rear=None
        
    def enqueue(self,data):
        new=Node(data)
        if self.rear is None:
            self.rear=new
            self.front=new
        else:
            self.rear.next=new
            self.rear=new
            
    def dequeue(self):
        if self.front is None:
            print("empty")
        else:
            temp=self.front.data
            self.front=self.front.next
            print(temp)
            
    def display(self):
        temp=self.front
        while temp:
            print(temp.data,end="--")
            temp=temp.next
        print(None)
        
q=queue(3)
q.enqueue("1")
q.enqueue("2")
q.enqueue("3")
q.display()
q.dequeue()
q.display()


