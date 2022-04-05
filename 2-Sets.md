# Sets

Sets are unique because they cant contain duplicate data and they don't have an order somethin is either iin the set or it's not in the set. These charateristics make sets more effecient in certain cases where we only need to know that data does or does not exist. These are the 2 main charteristacs that set a set apart (see what I did htere) from other data stuctures. 

## How Sets Work

Sets work by the use of hashing. A way to think of it is by to take a list of length 5 and assign its indexs A-E, with 'A' being index 0 and 'Z' being index 25, each index is empty.


|  -| - | - | - | -  |
|:---:|:---:|:---:|:---:|:---:|
|0|1|2|3|4|
|A|B|C|D|E|

## Adding to Set

Let's say we want to fill this list. To do this we will use a __hash function__. What a hash function will do is shorten an input and return it. This is very simplified and not practical, but for our example we will demonstrate it with a hash funtion that returns the index based on the first letter. For example if we sent in "Cat" which starts with C it will return 2, Because that is the index C coresponds with. Visualy our table would look like this:

|  - | - |Cat| - | - |
|:---:|:---:|:---:|:---:|:---:|
|0|1|2|3|4|
|A|B|C|D|E|

This same funtion would return 1 if "Bat" was entered. Notice how it will come before Cat even though it was added after, this is because, like we said before, sets dont dont care about order; instead they care about hash.

|  - |Dog|Cat| -  | -  |
|:---:|:---:|:---:|:---:|:---:|
|0|1|2|3|4|
|A|B|C|D|E|

As there are 26 letters lets take our imaginary hash function and have it retuen the index of any leter in the alphabet, not just the letters that corespond to out imaginary list. Words starting with the letters A-Z will be retuned as the numbers 0-25. __This is not yet our index__. To get our index we need to represent that number as a smaller number 0-4. This can be done very simply by using the modulus opertaion, ```hash_result % 5```. This would mean that Z would become __25__ through the hash function, and then __0__ from the modulus operation, while Y would become __4__ thorugh the same prosses. After adding "Zed", our set would become:

|Zebra|Dog|Cat| -  | -  |
|:---:|:---:|:---:|:---:|:---:|
|0|1|2|3|4|
|A|B|C|D|E|

### Checking Set for Value

We can check if the set contains something in O(1) time. If we wanted to check for "Ant" the hash and modulus funtions would get the index it would be found in and then it would compare the value there, "Zebra", to "Ant", returning false. Checking for "Cat" would do the same but would return true.


## Problems that May Occur when adding to set

You may have noticed in the example above that if we tried to add somthing to the set that started with Z, D, C, or any other letters that have the same value when modulated by 5, there wouldn't be a spot available in the set. These are called conflicts and there are a couple reasonable ways to overcome them, but both methods don't allow for 0(n) performance. 

### Opoen adressing
The first method is to put it in the next empty spot. For example if we wanted to add "Ape" to our set, indexes 0, 1, 2, and 3 would have to be checked for emptyness. 

|Zebra|Dog|Cat|Ape| -  |
|:---:|:---:|:---:|:---:|:---:|
|0|1|2|3|4|
|A|B|C|D|E|

Because this could potentialy happen for every index in the list, adding now becomes O(n). Aditionaly you would have to do the same for each 

### Chaining 

Chaining works by creating a list wherewver you have a collision. Instead of putting "Ape" at index 3 like above, we would create a list containing Ape and Zebra.

|[Zebra, Ape]|Dog|Cat|Ape| -  |
|:---:|:---:|:---:|:---:|:---:|
|0|1|2|3|4|
|A|B|C|D|E|

In this case adding is still O(1) but checking will become O(n) because you now have to search through a list.

### Resizing Set

With both of the above methods, there will eventualy come a point where it will be completely filled or the performance will become to slow. The only way to fix this will be to resize the list. The downside of doing this is that you will need to rehash every single value and add them to the new, larger, list.

## Functions

### Add

```python
set_name.add(value)
```

This will get the hash of the value and insert it in that index. It is O(1) because it doen't require looping through any lists.

### Remove

```python
set_name.remove(value)
```

This will get the hash of the value and if the value of the set at that index equals the value then that index will romove it by setting that spot to empty. This is also O(1) because no looping is required.

### Contains
```python
if value in set_name:
```

Returns true if the value at the hash index equals the value. This is also O(1) because no looping is required.

### Size

```python
len(set_name)
```

Returns the number of values in set. This is O(1) because you can you increemnt or decrement a variavle whenever you add or remove, respectivly, and return the value of it when this function is called.


## Example - Speed of checking 10000 random numbers with list vs set

The following code will generate 10000 random numbers and add them to both a list and set. When it has finished that it will count the numbers generated between 0 and 1000 using the set and then it will count them using the list. This will demonstate just how significant the difference in time efficiency is.

```python
#Define list
#Define Set
#Loop 10000 (more or less) time
    #generate random number
    #append number to list
    #add number to set

#count the numbers in set that fall in the range of 0 and 1000
#pritnt the amount of numbers
#print time it took

#Count the numbers in list that fall in the range of 0 and 1000
#pritnt the amount of numbers
#print time it took

#calculate time ratio between both
```

## Problem for you to Solve
