# Draw two triangles
from turtle import*

# Draw 1st triangle
for sides in range(1, 4):
                forward(40)
                left(120)

# Move to position of triangle 2
penup()
left(30)
forward(80)
left(90)
pendown()

# Draw 2nd triangle
for sides in range(1, 4):
                forward(40)
                left(120)
                
# Move to position of triangle 3
penup()
left(120)
forward(80)
pendown()

# Draw 3rd triangle
for sides in range(1, 4):
                forward(40)
                left(120)
