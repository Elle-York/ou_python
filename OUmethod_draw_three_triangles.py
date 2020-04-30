# Draw two triangles
from turtle import*

# Draw 1st triangle
for sides in range(1, 4):
                forward(40)
                left(120)

# Move to position of triangle 2
penup()
forward(100)
pendown()

# Draw 2nd triangle
for sides in range(1, 4):
                forward(40)
                left(120)
                
# Move to position of triangle 3
penup()
left(180)
forward(100)
right(90)
forward(100)
right(90)
pendown()

# Draw 3rd triangle
for sides in range(1, 4):
                forward(40)
                left(120)
