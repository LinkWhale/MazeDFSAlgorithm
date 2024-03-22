import turtle as t
import random

GridSize = 20


x, y = 0, 0

visited = [(x, y)]
stack = [(x, y)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while stack:

    x, y = stack[-1]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
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

for x, y in visited:
    t.penup()
    t.setpos(x*10, y*10)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

t.done()