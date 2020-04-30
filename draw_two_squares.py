# Draw two squares
from turtle import*

# Draw a square
for sides in range(1, 5):
                forward(40)
                right(90)

# Move to start of next square
penup()
right(90)
forward(50)
left(90)
pendown()

# Draw a square
for sides in range(1, 5):
                forward(40)
                right(90)
