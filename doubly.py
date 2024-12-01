class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None

    def insertFirst(self,data):
        new=Node(data)
        new.next=self.head
        self.head.prev=new
        self.head=new

    def insertLast(self,data):
        new=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
        new.prev=temp

    def insertPos(self,pos,data):
        new=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        new.next=temp.next
        temp.next.prev=new
        temp.next=new
        new.prev=temp

    def deleteFirst(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None

    def deleteLast(self):
        temp=self.head.next
        before=self.head
        while temp.next is not None:
            temp=temp.next
            before=before.next
        before.next=None
        temp.prev=None

    def deletePos(self,pos):
        temp=self.head.next
        before=self.head
        for i in range(1,pos-1):
            temp=temp.next
            before=before.next
        before.next=temp.next
        temp.next.prev=before.next
    
    def display(self):
        if self.head is None:
            print("empty dll")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
L=DLL()
n=Node(10)
L.head=n
L.insertFirst(5)
L.insertLast(50)
L.insertPos(3,20)
L.insertPos(4,30)
L.insertPos(5,40)
L.display()
L.deleteFirst()
L.deleteLast()
L.deletePos(3)
L.display()
