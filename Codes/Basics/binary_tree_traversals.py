'''
            1
          /    \
          2     3
         / \   /  \
        4   5 6    7
        
'''
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self. right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def print_tree(self, traversal_type, root):
        if traversal_type == 'pre-order':
            print(self.preorder_traversal(root, "").rstrip(" - "))
        elif traversal_type == 'in-order':
            print(self.inorder_traversal(root, "").rstrip(" - "))
        elif traversal_type == 'post-order':
            print(self.postorder_traversal(root, "").rstrip(" - "))
        else:
            return False
    
    def preorder_traversal(self, item, traversal):
        if item:
            traversal += str(item.val) + " - "
            traversal = self.preorder_traversal(item.left, traversal)
            traversal = self.preorder_traversal(item.right, traversal)
        return traversal
    
    def inorder_traversal(self, item, traversal):
        if item:
            traversal = self.inorder_traversal(item.left, traversal)
            traversal += str(item.val) + " - "
            traversal = self.inorder_traversal(item.right, traversal)
        return traversal
    
    def postorder_traversal(self, item, traversal):
        if item:
            traversal = self.postorder_traversal(item.left, traversal)
            traversal = self.postorder_traversal(item.right, traversal)
            traversal += str(item.val) + " - "
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.print_tree("pre-order", tree.root)
tree.print_tree("in-order", tree.root)
tree.print_tree("post-order", tree.root)

