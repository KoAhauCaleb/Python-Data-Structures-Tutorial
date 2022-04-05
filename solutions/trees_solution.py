from random import randint
import time

class CustomSet:
    
    def __init__(self, size = 1000):
        self.size = size
        self.values = [None for i in range(size)]
        self.value_count = 0
        self.conflict_count = 0

    def hash(self, value):
        hash = (value % self.size)
        return hash

    def add(self, value):
        if not self.conflict(value):
            self.values[self.hash(value)] = value
            self.value_count += 1

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
        self.node_count = 0
        self.value_count = 0

    def add(self, value):
        self._add(self.root, value)

    def _add(self, node, value):
        
        if not node.values.conflict(value):
            node.values.add(value)
            self.value_count += 1
            return

        if node.values.conflicting_val(value) > value:
            if node.right is None:
                node.right = self.Node()
                self.node_count += 1
            self._add(node.right, value)

        elif node.values.conflicting_val(value) < value:
            if node.left is None:
                node.left = self.Node()
                self.node_count += 1
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

set_tree = SetTree()
fast_set = CustomSet(1000)
slow_list = []

list_init_start_time = time.perf_counter()
for i in range(100000):
    random = randint(0, 1000000)
    slow_list.append(random)
list_init_end_time = time.perf_counter()
list_init_time = list_init_end_time - list_init_start_time
print(f"{list_init_time=}")

tree_init_start_time = time.perf_counter()
for num in slow_list:
    set_tree.add(num)
tree_init_end_time = time.perf_counter()
tree_init_time = tree_init_end_time - tree_init_start_time
print(f"{tree_init_time=}")

set_init_start_time = time.perf_counter()
for num in slow_list:
    fast_set.add(num)
set_init_end_time = time.perf_counter()
set_init_time = set_init_end_time - set_init_start_time
print(f"{set_init_time=}")

print("--------------------")

list_count_start_time = time.perf_counter()
list_count = 0
for i in range(10001):
    if i in slow_list:
        list_count += 1
list_count_end_time = time.perf_counter()
list_count_time = list_count_end_time - list_count_start_time
print(f"{list_count_time=}")

tree_count_start_time = time.perf_counter()
tree_count = 0
for i in range(10001):
    if set_tree.contains(i):
        tree_count += 1
tree_count_end_time = time.perf_counter()
tree_count_time = tree_count_end_time - tree_count_start_time
print(f"{tree_count_time=}")

set_count_start_time = time.perf_counter()
set_count = 0
for i in range(10001):
    if fast_set.contains(i):
        set_count += 1
set_count_end_time = time.perf_counter()
set_count_time = set_count_end_time - set_count_start_time
print(f"{set_count_time=}")

print("--------------------")

print(f"{set_tree.node_count=}")
print(f"{set_tree.value_count=}")

print("")

print(f"{len(slow_list)=}")

print("")

print(f"{fast_set.value_count=}")

print("--------------------")
