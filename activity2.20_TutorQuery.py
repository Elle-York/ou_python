
# Activity 2.20 Nested loops...

####################################################

# My understanding of what is happening. 

# Line 1) create rows, range is start at 1, stop at 4 (therefore no of rows = 3)
# Line 2) for every new row, create a space
#    for first row range is start at 1, stop at (3 - 1 row) + 1 = range 1 to 3 (2 spaces)
#    for second row range is start at 1, stop at (3 - 2 rows) + 1 = range 1 to 2 (1 space)
#    for third row  range is start at 1, stop at (3 - 3 rows) + 1 = range 1 to 1 (0 space)
# Line 3) each space on each row should be blank, then append a space
# Line 4) for every new row create a column with an asterisk,
#    for first column, range is start at 1, stop at 1 row + 1) = range 1 to 2 (1 asterisk)
#    for second column, range is start at 1, stop at 2 row + 1) = range 1 to 3 (2 asterisk)
#    for third column, range is start at 1, stop at 3 row + 1) = range 1 to 4 (3 asterisk)
# Line 5) print asterisk in every column, then append a space
# Line 6) prints a new line



# Bottom right right angle triangle

size = 3

for row in range(1, size + 1): # Line 1
    for space in range(1, size - row + 1): # Line 2
        print(' ', end = '') # Line 3
    for column in range(1, row + 1): # Line 4
        print('*', end = '') # Line 5
    print() # Line 6




 


    
