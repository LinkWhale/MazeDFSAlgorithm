import turtle as t
import random

GridSize = 20

x, y = 0, 0

visited = [(x, y)] #contains every visited space in order they generate in
stack = [(x, y)] #stack for the DPS algorithm

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] #directions a path can go

#Generation loop
while stack:

    x, y = stack[-1]
    random.shuffle(directions)

    for dx, dy in directions: #dx and dy stand for direction x and direction y
        nx, ny = x + dx, y + dy #nx and ny stand for new x and new y

        #contains the maze within borders and makes sure the space wasnt visited
        if nx >= 0 and nx <= GridSize and ny >= 0 and ny <= GridSize and (nx +dx, ny +dy) not in visited:
            visited.append((nx, ny))
            visited.append((nx + dx, ny + dy))
            stack.append((nx + dx, ny + dy))
            break
    else:
        stack.pop()
    
t.Screen().bgcolor("black")
t.hideturtle()
t.color("white")
t.speed(0)

#places a circle in every visited coordinate
for x, y in visited:
    t.penup()
    t.setpos(x*10, y*10)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

t.done()