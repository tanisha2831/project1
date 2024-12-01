class Node:
    def _init_(self, key):
        self.key = key
        self.left = None
        self.right = None

    def inorder(root):
        if root:
            Node.inorder(root.left)
            print(root.key, end=" ")
            Node.inorder(root.right)

    def preorder(root):
        if root:
            print(root.key, end=" ")
            Node.preorder(root.left)
            Node.preorder(root.right)

    def postorder(root):
        if root:
            Node.postorder(root.left)
            Node.postorder(root.right)
            print(root.key, end=" ")

    def search(root, key):
        if root is None:
            return False 
        if root.key == key:
            return True  
        if key < root.key:
            return Node.search(root.left, key)
        return Node.search(root.right, key) 

root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(17)
root.right.right = Node(25)

print("Inorder Traversal:")
Node.inorder(root)
print("\nPreorder Traversal:")
Node.preorder(root)
print("\nPostorder Traversal:")
Node.postorder(root)
print("\nSearching in BST:")
search_key = 12
print(f"Element {search_key} found:"
      if Node.search(root, search_key)
      else f"Element {search_key} not found.")
