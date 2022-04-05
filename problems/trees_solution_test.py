from random import randint
import time

#Replace this with CustomSet class.

#Replace this with the modified BinaryTree class named SetTree.

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
