# Queues
The way a queue work is *first in - first out*. Basically it a list where you're limited to getting and removing the first element, and appending an element to the end. This is useful for things like: 

* When data need to processed be in order.
* When you are working with something external that has a limited speed.

It is easy to remember if you think of a checkout line. The first person to get there will be the first person to be served. If you join the line when there are 9 people in it, then 9 people have to checkout before you can check out.

An example of what it would not be is a stack of pancakes. That is represented by a data structure, called a stack. A stack is different because it's *last in - first out*. Basically the most recent pancake cooked will be the first pancake served. That's all I'll say about stacks here, I encourage you to research them yourself after reading this chapter as they are very closely related to queues.
## __Functions__

The are several functions that a queue used, discussed in the following sections:

*Note: Queues in python are just lists where you limit your use to only certain functions. Because of this you will likely recognize all of these functions if you already have experience with python.*

### Enqueue
__Adds a value to the end of a list.__ 

The following code is how it would vbe used in python:

```python
queue.append(value)
```

In other languages you may see enqueue(value) instead, or even something completely different. 

This functions performance is O(1) even though the list can change size because by adding in to the end, you won't need to change the index of any other values

### Dequeue

__Removes and returns value form end of list.__ 

There are two ways tpo represent in python:

```python
value = queue[0]
delete queue[0]
```

-or- 

```python
value = queue.pop(0)
```

This has is a performance of O(n), this is because when removing the first value, you also will need to go through every other value and decrease the index by one.

*Note: This can be O(1) when implemented correctly. This requires an understanding of linked list though, which I don't cover in this tutorial, but it's essentially a 1D tree, covered in chapter 3, meaning nodes only have a single child. By setting the child of the linked lists root to the root, you are moving each value forward one without having to check each of them, and getting rid of the first value.*

### Size

__Returns the amount of values in list.__

In python it would be:

```python
size = len(queue)
```

This is O(1) because instead of needing to count each value int the queue you just need to keep track of how many values you have enqueued and dequeued

### Empty

returns true if there are no values in the queue

```python
if len(queue) == 0:
    pass
```

This is O(1) because it's the result of the size function compared with zero.

## Example 

As an example of how this works lets look at a program where we have a slow moving
turtle. We want to give the turtle directions to create a star in the sand.
Each command will contain a number of steps and the amount of degrees to turn after
completing those steps. Because a turtle is slow and can't immediately follow a command
like a computer can, this will be a good situation to use a queue.

This is demonstrated by the following code:
```python
from time import sleep
import turtle

#Move turtle forward one step at a time.
def forward(t, steps):
    for i in range(steps):
        t.forward(1)

#Rotate turtle right one step at a time.
def right(t, steps):
    for i in range(steps):
        t.right(1)

points = int(input("Enter the amount of points you want your star to have: "))

screen = turtle.getscreen()
t= turtle.Turtle()
t.shape("turtle")
t.fillcolor("green")

rotation_queue = []

step_queue = [100, 100, 100, 100, 100]

point_angle = int(180 / points)

if (points / 2) % 2 == 0:
    point_angle = int(360 / points)

rotate_angle = 180 - point_angle

#For each point, add the degrees of rotation to the queue.
for i in range(points - 1):
    rotation_queue.append(rotate_angle)     #This is O(1).

'''
For each angle in the rotation queue, walk forward and turn the degrees specified by the next
value in the queue.
'''
forward(t , 100)
while len(rotation_queue) > 0:              #Getting queue length: O(1), Loop: O(n)
    rotation = rotation_queue.pop(0)        #This is O(1).

    right(t, rotation)
    forward(t , 100)


#Keep open until X button pressed.
turtle.exitonclick()
turtle.mainloop()
```


## Problem for you to solve

In the folloing code ... needs to be implemented. the reqirements for the program are:

- Create graphics to help them understand the problem better.

You can view and download the incomplete template code at [link](www.link.link)

You can view and download the solution at [link](www.link.link)

