class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None

    def insertFirst(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    def insertLast(self,data):
        nl=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=nl

    def insertPos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np

    def deleteFirst(self):
        temp=self.head
        self.head=temp.next
        temp=None
        
    def deleteLast(self):
        temp=self.head.next
        prev=self.head
        while temp.next:
            temp=temp.next
            prev=prev.next
        prev.next=None

    def deletePos(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
    
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
L=Sll()
n=Node(10)
L.head=n
L.insertFirst(5)
L.insertLast(20)
L.insertPos(3,25)
L.display()

L.deleteFirst()
L.deleteLast()
L.deletePos(3)
L.display()
