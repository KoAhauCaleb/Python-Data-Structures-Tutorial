# Queues
The way a queue work is first in firwst out. 
Basicicaly jsut a list limited to that.this is usefull for things like... 

-when data need to prossesed be in order.
-when you are working with somethink external that has a limited speed.

It is easy to remember if you think of a shopping line, or queue as they would say in austrailia (I'm assuming that's how austrains speak)

## __Functions__

------- Maybe turn this into a table???------

The are sesveral functions that a queue used, disscusseed in the following sections:

*Note: Queues in pyhon are just lists where you limit your use to only certain functions. Because of this you will likely recognize all of these functions if you allreu have experience with python. /itlaicize*

### Enqueue
The enqueue function adds a value to the end of a list. 

The following code is how it would vbe used in python:

```python
queue.append(value)
```

In other languages you may see enqueue(value) instead, or even something completely different. 

This function performance is O(1) even though the list can change size because by adding in to the end, you won't need to change the index of any other values

### Dequeue

reomoves and returns value form end of list. 

there are two ways tpo represent in ptthon:

```python
value = queue[0]
delete queue[0]
```

-or- 

```python
value = queue.pop(0)
```

This is a performance of O(n), this is because when removing the first value, you also will need to go through every other value and decrease the index by one.

Note that this can be O(1) when implemented correctly. This requires an understanding of linked list though, which I currently not going over in this tutorial, but it's essentially a 1D tree, covered in chapter 3, meaning nodes only have a single child. By setting the child of the root to the 

### Size

Returns the amount of values in list. 

In python it would be:

```python
size = len(queue)
```

This is O(1) because instead of needing to count each value int he queue you jsut need to keep track of how many values you have enqued and dequeued

### Empty

returns true if there are no values in the queue

```python
if len(queue) == 0:
    pass
```

O(1) because same as size just compared with zero.

## Example Problem 

As an example of how this works lets look at a program where we have a slow moving
turtle. We want to give the turtle directions to create a star in the sand.
Each cammand will contain a number of steps and the amount of degrees to turn after
completing those steps. Because a turtle is slow and can't imediatly follow a cammand
like a computer can, this will be a good situation to use a queue.

We will start out with the followng code:
```python

```


## Problem for you to solve

In the folloing code ... needs to be implemented. the reqirements for the program are:

- Create graphics to help them understand the problem better.

You can view and download the incomplete template code at [link](www.link.link)

You can view and download the solution at [link](www.link.link)

