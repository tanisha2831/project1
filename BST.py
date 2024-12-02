class node:
    def _init_(self,val):
        self.lchild=None
        self.data=val
        self.rchild=None
class btree:
    def _init_(self):
        self.root=None
    def insert(self,val):
        temp=node(val)
        trv=self.root
        if self.root is None:
            self.root=temp
            return
        else:
            while True:
                if(val > trv.data):
                    if trv.rchild is None:
                        trv.rchild=temp
                        return
                    else:
                        trv=trv.rchild
                else:
                    if trv.lchild is None:
                        trv.lchild=temp
                        return
                    else:
                        trv=trv.lchild
    def search(self,key):
        trv=self.root
        while True:
            if trv is None:
                return False
            if trv.data==key:
                return True
            if trv.data<key:
                trv=trv.rchild
            else:
                trv=trv.lchild
def inorder(self,rt):
        if rt is not None:
            self.inorder(rt.lchild)
            print(rt.data,end=" ")
            self.inorder(rt.rchild)
    def preorder(self,rt):
        if rt is not None:
            print(rt.data,end=" ")
            self.preorder(rt.lchild)
            self.preorder(rt.rchild)  
    def postorder(self,rt):
        if rt is not None:
            self.postorder(rt.lchild)
            self.postorder(rt.rchild)
            print(rt.data,end=" ")
bst=btree()
bst.insert(10)
bst.insert(5)
bst.insert(20)
bst.insert(50)
bst.insert(30)
bst.insert(40)
bst.insert(35)
print("Inorder")
bst.inorder(bst.root)
print("\nPreorder")
bst.preorder(bst.root)
print("\nPostorder")
bst.postorder(bst.root)
bst.search(10)
print("\nElement is searched:",bst.search(10))
