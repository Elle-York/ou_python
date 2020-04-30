# Produce graph for glove sales
from turtle import*

# Set up glove sales variable
gloves1 = 10
gloves2 = 8
gloves3 = 3
gloves4 = 5

totalgloves = gloves1 + gloves2+ gloves3 + gloves4
print(totalgloves)

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

# variable that holds a list of numbers
gloves = [10, 8, 3, 5]

# Access values in my list
print(gloves[0])
print(gloves[1])
print(len(gloves))

# Calculate total glove sales
total = 0                                                                  # Sets initial variable to 0
for index in range (len(gloves)):                     # considers the 4 values in the variable 'gloves'  
                total = total + gloves [index]           # starts at 0 and adds all the values in the range

print(total)

# Reverse the list using a function
gloves.reverse()
print('Updated List:', gloves)

# Reverse the list using OUs stupid method
gloves = [10, 8, 3, 5]
temp1 = gloves[0]
gloves[0] = gloves[3]
gloves[3] = temp1
temp2 = gloves[1]
gloves[1] = gloves[2]
gloves[2] = temp2
print(gloves)
