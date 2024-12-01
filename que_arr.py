class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, data):
        self.queue.append(data)
        
    def dequeue(self):
        if len(self.queue) == 0:
            print("empty")
        else:
            temp = self.queue.pop(0)
            print(temp)
            
    def display(self):
        print("-".join(self.queue))


q = Queue()
q.enqueue("1")
q.enqueue("2")
q.enqueue("3")
q.display() 
q.dequeue()
q.display()  
