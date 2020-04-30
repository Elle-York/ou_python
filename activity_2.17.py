# Produce graph for glove sales
from turtle import*

# Set up glove sales variable
gloves = [10, 8, 3, 5]

# Produce x-axis
goto(80, 0)

# Produce y-axis
goto(0, 0)
goto(0, 100)

# Plot data
goto(0, 0)
for index in range(len(gloves)):
                goto(20 + (20 * index), gloves[index] * 10)

# Go to  0 on graph for y and x
# Then count length = 4
# Then for the 4 numbers in the variable
# go to x = increase by multiples of 20
# go to y axis = each number in variable times 10


