from random import randint
import time

class CustomSet:
    
    def __init__(self):
        self.values = [None for i in range(100)]

    def hash(self, value):
        hash = (value % 100)
        return hash

    def insert(self, value):
        if not self.conflict(value):
            self.values[self.hash(value)] = value

    def contains(self, value):
        if self.conflicting_val(value) == value:
            return True
        return False

    def conflicting_val(self, value):
        return self.values[self.hash(value)]

    def conflict(self, value):
        if self.conflicting_val(value) is not None:
            return True
        return False
        

class SetTree:

    class Node:
        
        def __init__(self):
            self.values = CustomSet()
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = self.Node()

    def add(self, value):
        self._add(self.root, value)

    def _add(self, node, value):
        
        if not node.values.conflict(value):
            node.values.insert(value)
            return

        if node.values.conflicting_val(value) > value:
            if node.right is None:
                node.right = self.Node()
            self._add(node.right, value)

        elif node.values.conflicting_val(value) < value:
            if node.left is None:
                node.left = self.Node()
            self._add(node.left, value)  
        
    def contains(self, value):
        return self._contains(self.root, value)

    def _contains(self, node, value):
        
        if node.values.contains(value):
            return True
        elif node.values.conflicting_val(value) is None:
            return False
        
        if node.values.conflicting_val(value) > value:
            if node.right is None:
                return False
            return self._contains(node.right, value)

        if node.values.conflicting_val(value) < value:
            if node.left is None:
                return False
            return self._contains(node.left, value) 

bt = SetTree()

bt.add(10)
bt.add(110)
bt.add(100)
bt.add(99)
bt.add(12)
bt.add(9)

slow_list = []

for i in range(10000):
    random = randint(0, 100000)
    bt.add(random)
    slow_list.append(random)

count = 0
for i in range(1001):
    if bt.contains(i):
        count += 1

print(count)

count = 0
for i in range(1001):
    if i in slow_list:
        count += 1
        
print(count)
