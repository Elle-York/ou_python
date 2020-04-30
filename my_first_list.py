
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






