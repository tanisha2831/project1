class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
        self.prev = None  

class DCLL:
    def __init__(self):
        self.head = None  
        self.tail = None  

    def insertFirst(self, data):
        n = Node(data)
        if self.head is None:  
            self.head = n
            self.tail = n
            n.next = n
            n.prev = n
        else:
            n.next = self.head
            n.prev = self.tail
            self.head.prev = n
            self.tail.next = n
            self.head = n
        print(f"Inserted {data} at the beginning")

    def insertLast(self, data):
        n = Node(data)
        if self.head is None: 
            self.head = n
            self.tail = n
            n.next = n
            n.prev = n
        else:
            n.prev = self.tail
            n.next = self.head
            self.tail.next = n
            self.head.prev = n
            self.tail = n
        print(f"Inserted {data} at the end")

    def insertPos(self, pos, data):
        if pos == 1:
            self.insertFirst(data)
            return
        n = Node(data)
        temp = self.head
        for i in range(1, pos - 1):
            temp = temp.next
        n.next = temp.next
        n.prev = temp
        temp.next.prev = n
        temp.next = n
        print(f"Inserted {data} at position {pos}")

    def deleteFirst(self):
        if self.head is None: 
            print("List is empty")
        elif self.head == self.tail: 
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            temp = None
        print("Deleted the first node")

    def deleteLast(self):
        if self.head is None: 
            print("List is empty")
        elif self.head == self.tail: 
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            temp = None
        print("Deleted the last node")

    def deletePos(self, pos):
        if self.head is None: 
            print("List is empty")
        elif pos == 1: 
            self.deleteFirst()
        else:
            temp = self.head
            for i in range(1, pos):
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp = None
            print(f"Deleted node at position {pos}")

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            print(f"{temp.data} --> ", end="")
            temp = temp.next
            while temp != self.head:
                print(f"{temp.data} --> ", end="")
                temp = temp.next
            print(f"(back to head: {self.head.data})")

L = DCLL()
L.insertFirst(10)
L.insertLast(50)
L.insertPos(2, 20)
L.insertPos(1, 5)
L.display()
L.deleteFirst()
L.deleteLast()
L.deletePos(2)
L.display()
