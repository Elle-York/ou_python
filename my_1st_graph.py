# Produce graph for glove sales
from turtle import*

# Set up glove sales variable
gloves1 = 10
gloves2 = 8
gloves3 = 3
gloves4 = 5

# Produce x-axis
goto(100, 0)

# Produce y-axis
goto(0, 0)
goto(0, 100)

# Plot data
goto(0, 0)
goto(25, gloves1 * 10)
goto(50, gloves2 * 10)
goto(75, gloves3 * 10)
goto(100, gloves4 * 10)

