
# Draw a line of triangles across the page increasing in size

from turtle import *
number_of_triangles = 4

for shape in range(1, number_of_triangles + 1):
    
    # Draw a triangle
    for sides in range(1, 4): 
        forward(20 * shape) 
        left(120)

    # move forward to start position of next triangle
    penup()
    left(60)
    forward(20 * shape + 10)
    right(60)
    pendown()
