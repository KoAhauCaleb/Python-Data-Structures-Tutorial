# Sets

Sets are unique because they can't contain duplicate data and they don't have an order, something is either in the set or it's not in the set. These characteristics make sets more efficient in certain cases where we only need to know that data does or does not exist. These are the 2 main characteristics that set a set apart (see what I did there) from other data structures. 

## How Sets Work

Sets work by the use of hashing. A way to think of it is by to take a list of length 5 and assign its indexes A-E, with 'A' being index 0 and 'Z' being index 25, each index is empty.


|  -| - | - | - | -  |
|:---:|:---:|:---:|:---:|:---:|
|0|1|2|3|4|
|A|B|C|D|E|

## Adding to Set

Let's say we want to fill this list. To do this we will use a __hash function__. What a hash function will do is shorten an input and return it. This is very simplified and not practical, but for our example we will demonstrate it with a hash function that returns the index based on the first letter. For example if we sent in "Cat" which starts with C it will return 2, Because that is the index C corresponds with. Visually our table would look like this:

|  - | - |Cat| - | - |
|:---:|:---:|:---:|:---:|:---:|
|0|1|2|3|4|
|A|B|C|D|E|

This same function would return 1 if "Bat" was entered. Notice how it will come before Cat even though it was added after, this is because, like we said before, sets don't care about order; instead they care about hash.

|  - |Dog|Cat| -  | -  |
|:---:|:---:|:---:|:---:|:---:|
|0|1|2|3|4|
|A|B|C|D|E|

As there are 26 letters lets take our imaginary hash function and have it return the index of any letter in the alphabet, not just the letters that correspond to out imaginary list. Words starting with the letters A-Z will be returned as the numbers 0-25. __This is not yet our index__. To get our index we need to represent that number as a smaller number 0-4. This can be done very simply by using the modulus operation, ```hash_result % 5```. This would mean that Z would become __25__ through the hash function, and then __0__ from the modulus operation, while Y would become __4__ through the same process. After adding "Zebra", our set would become:

|Zebra|Dog|Cat| -  | -  |
|:---:|:---:|:---:|:---:|:---:|
|0|1|2|3|4|
|A|B|C|D|E|

### Checking Set for Value

We can check if the set contains something in O(1) time. If we wanted to check for "Ant" the hash and modulus functions would get the index it would be found in and then it would compare the value there, "Zebra", to "Ant", returning false. Checking for "Cat" would do the same but would return true.


## Problems that May Occur when adding to set

You may have noticed in the example above that if we tried to add something to the set that started with Z, D, C, or any other letters that have the same value when modulated by 5, there wouldn't be a spot available in the set. These are called conflicts and there are a couple reasonable ways to overcome them, but both methods don't allow for 0(n) performance. 

### Open Addressing
The first method is to put it in the next empty spot. For example if we wanted to add "Ape" to our set, indexes 0, 1, 2, and 3 would have to be checked for emptiness. 

|Zebra|Dog|Cat|Ape| -  |
|:---:|:---:|:---:|:---:|:---:|
|0|1|2|3|4|
|A|B|C|D|E|

Because this could potentially happen for every index in the list, adding now becomes O(n). Additionally you would have to do the same for each 

### Chaining 

Chaining works by creating a list wherever you have a collision. Instead of putting "Ape" at index 3 like above, we would create a list containing Ape and Zebra.

|[Zebra, Ape]|Dog|Cat|Ape| -  |
|:---:|:---:|:---:|:---:|:---:|
|0|1|2|3|4|
|A|B|C|D|E|

In this case adding is still O(1) but checking will become O(n) because you now have to search through a list.

### Resizing Set

With both of the above methods, there will eventually come a point where it will be completely filled or the performance will become to slow. The only way to fix this will be to resize the list. The downside of doing this is that you will need to rehash every single value and add them to the new, larger, list.

## Functions

### __Add__

```python
set_name.add(value)
```

This will get the hash of the value and insert it in that index. It is O(1) because it doesn't require looping through any lists.

### __Remove__

```python
set_name.remove(value)
```

This will get the hash of the value and if the value of the set at that index equals the value then that index will remove it by setting that spot to empty. This is also O(1) because no looping is required.

### __Contains__
```python
if value in set_name:
```

Returns true if the value at the hash index equals the value. This is also O(1) because no looping is required.

### __Size__

```python
len(set_name)
```

Returns the number of values in set. This is O(1) because you can you increment or decrement a variable whenever you add or remove, respectively, and return the value of it when this function is called.


## Example - Speed of checking 10000 random numbers with list vs set

The following code will generate 10000 random numbers and add them to both a list and set. When it has finished that it will count the numbers generated between 0 and 1000 using the set and then it will count them using the list. This will demonstrate just how significant the difference in time efficiency is.

```python
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
```

This is one example of the results I get when running this:

```
Numbers generated between 0 and 1000 inclusive: 88
--------------------
Amount of unique numbers between 1 and 1000 in set: 86
Time taken to check set: 0.060 ms
--------------------
Amount of unique numbers between 1 and 1000 in list: 86
Time taken to check set: 73.521 ms
--------------------
The set is 1215.221487603345 times faster than the list.
```

The results are different for each run, but the set is anywhere from 600 to 1400 times faster than using the list for the same problem.

## Problem for you to Solve
In the following code you will create your own set class by finishing the functions add and contains based on what their description is.

If you would like a greater challenge, follow this [link](problems/set_problem_hard.py) for a harder version of the following code. Don't look at the following code!

```python
class CustomSet:
    
    def __init__(self, size = 1000):
        self.size = size
        self.values = [None for i in range(size)]
        self.value_count = 0
    
    '''
    Return the hash of a value.
    '''
    def hash(self, value):
        hash = (value % self.size)
        return hash

    '''
    If there is no conflict, add value to set at the index of it's hash. Return false if
    there is a conflict, or value is already in the set.
    '''
    def add(self, value):
        pass
    
    '''
    If the set contains value, return true. If not, return false.
    '''
    def contains(self, value):
        pass

    '''
    Return the value at the same hash as the passed value.
    '''
    def val_at_hash(self, value):
        return self.values[self.hash(value)]

    '''
    Return true if index of value's hash is has been set, otherwise the function returns false.
    '''
    def conflict(self, value):
        if self.val_at_hash(value) is not None:
            return True
        return False


#Test Case:
my_set = CustomSet()

for i in range(0, 6, 2):
    my_set.add(i)

for i in range(7):
    print(my_set.contains(i))
```
You should get the following result when running it in the command line:

```
True
False
True
False
True
False
False
```

When you are finished or stuck, you can find my solution [here](solutions/set_solution.py).