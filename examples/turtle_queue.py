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
while len(rotation_queue) > 0:
    rotation = rotation_queue.pop(0)        #This is O(1).

    right(t, rotation)
    forward(t , 100)


#Keep open until X button pressed.
turtle.exitonclick()
turtle.mainloop()