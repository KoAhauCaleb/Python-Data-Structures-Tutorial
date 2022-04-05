import time

from random import randint

slow_list = []
fast_set = set()

#Add 10000 random numbers between 0 and 100000.
count_less_eq_1000 = 0
for i in range(10000):
    rand_num = randint(0, 100000)

    if rand_num <= 1000:
        count_less_eq_1000 += 1

    slow_list.append(rand_num)
    fast_set.add(rand_num)

print(f"Numbers generated between 0 and 1000 inclusive: {count_less_eq_1000}")

#Count the amount of unique values between 0 and 1000 inclusive in the set.
set_count = 0
set_start_time = time.perf_counter()

for i in range(1001):               #This is O(n) time efficiency.
    if i in fast_set:               #This is O(1) time efficiency.
        set_count += 1              #In total this would be O(n*1) or O(n) time efficency.
set_end_time = time.perf_counter()

#Show set statistics.
print("--------------------")
print(f"Amount of unique numbers between 1 and 1000 in set: {set_count}")

set_time_taken = (set_end_time - set_start_time)
print(f"Time taken to check set: {(set_time_taken * 1000):.3f} ms")

#Count the amount of unique values between 0 and 1000 inclusive in the list.
list_count = 0
list_start_time = time.perf_counter()
for i in range(1001):               #This is O(n) time efficiency.
    if i in slow_list:              #This is O(n) time efficiency.
        list_count += 1             #In total this would be O(n*n) or O(n^2) time efficency.
list_end_time = time.perf_counter()

#Show list statistics.
print("--------------------")
print(f"Amount of unique numbers between 1 and 1000 in list: {list_count}")

list_time_taken = (list_end_time - list_start_time)
print(f"Time taken to check set: {(list_time_taken * 1000):.3f} ms")

print("--------------------")
time_ratio = list_time_taken / set_time_taken
print(f"The set is {time_ratio} times faster than the list.")