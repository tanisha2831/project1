class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SCLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def insertFirst(self,data):
        n=Node(data)
        n.next=self.head
        self.tail.next=n
        self.head=n

    def insertLast(self,data):
        n=Node(data)
        self.tail.next=n
        self.tail=n
        self.tail.next=self.head

    def insertPos(self,pos,data):
        n=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.next=temp.next
        temp.next=n

    def deleteFirst(self):
        temp=self.head
        self.head=temp.next
        self.tail.next=temp.next
        temp=None

    def deleteLast(self):
        temp=self.head
        while temp.next!=self.tail:
            temp=temp.next
        self.tail=None
        self.tail=temp
        temp.next=self.head

    def deletePos(self,pos):
        temp=self.head.next
        before=self.head
        for i in range(1,pos-1):
            temp=temp.next
            before=before.next
        before.next=temp.next
        temp=None
        
        
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            print(temp.data,"-->",end=" ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"-->",end=" ")
            print(temp.next.data)
L=SCLL()
n=Node(10)
L.head=n
L.tail=n
L.tail.next=L.head
L.insertFirst(5)
L.insertLast(50)
L.insertPos(3,20)
L.display()
L.deleteFirst()
L.deleteLast()
L.deletePos(3)
L.display()
