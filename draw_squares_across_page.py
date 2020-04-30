# Draw a line of squares across the page
from turtle import*
number_of_shapes = 4

for shape in range(1, number_of_shapes + 1):
    for sides in range(1, 5):
        forward(40)
        right(90)
    penup()
    forward(50)
    pendown()


# Draw a line of squares across the page - increasing in size
from turtle import*
number_of_shapes = 3

for shape in range(1, number_of_shapes + 1):
    for sides in range(1, 5):
        forward(30 + shape * 10)
        right(90)
    penup()
    forward(40 + shape * 10)
    pendown()
