# Draw a line of trianges across the page
# Independent nested loop - page 112 of part 2
from turtle import*
number_of_shapes = 3

for shape in range(1, number_of_shapes + 1):
    for sides in range(1, 4): # 3 sides = triangle
        forward(40)
        left(120)
    penup()
    forward(50)
    pendown()

# Draw a line of triangles across the page increasing in size

from turtle import*
number_of_shapes = 3

for shape in range(1, number_of_shapes + 1): # no of shapes
    for sides in range(1, 4): # no of sides
        forward(30 + shape * 10)
        left(120)
    penup()
    forward(40 + shape * 10)
    pendown()
