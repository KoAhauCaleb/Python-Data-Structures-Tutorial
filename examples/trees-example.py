
class BinaryTree:

    class Node:
        
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None

    def add(self, value):
        node_to_add = self.Node(value)
        if self.root == None:
            self.root = node_to_add
            return
        
        self._add(self.root, node_to_add)

    def _add(self, node, new_node):
        
        if node.value > new_node.value:
            if node.right is None:
                node.right = new_node
            else:
                self._add(node.right)

        if node.value < new_node.value:
            if node.left is None:
                node.left = new_node
            else:
                self._add(node.left)        
        
    def contains(self, value):
        return self._contains(self.root, value)

    def _contains(self, node, value):
        
        if node.value == value:
            return True
        
        if node.value > value:
            if node.right is None:
                return False
            return self._contains(node.right, value)

        if node.value < value:
            if node.left is None:
                return False
            return self._contains(node.left, value) 

bt = BinaryTree()

bt.add(10)
bt.add(12)
bt.add(9)

print(bt.contains(9))
print(bt.contains(10))
print(bt.contains(11))
print(bt.contains(12))