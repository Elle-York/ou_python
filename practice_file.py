
# 1) create rows, range is start at 1, stop at 4 (therefore no of rows = 3)
# 2) for every new row, create a space
#    for first row range is start at 1, stop at (3 - 1 row) + 1 = range 1 to 3 (2 spaces)
#    for second row range is start at 1, stop at (3 - 2 rows) + 1 = range 1 to 2 (1 space)
#    for third row  range is start at 1, stop at (3 - 3 rows) + 1 = range 1 to 1 (0 space)
# 3) each space on each row should be blank, then append a space
# 4) for every new row create a column with an asterisk,
#    for first column, range is start at 1, stop at 1 row + 1) = range 1 to 2 (1 asterisk)
#    for second column, range is start at 1, stop at 2 row + 1) = range 1 to 3 (2 asterisk)
#    for third column, range is start at 1, stop at 3 row + 1) = range 1 to 4 (3 asterisk)
# 5) print asterisk in every column, then append a space
# 6) prints a new line


# 1st triangle - bottom left right angle

size = 3 
for row in range(1, size + 1): # 1
    for column in range(1, row + 1): # 4
        print('x', end = '') # 5
    print() # 6


# 2nd triangle - top right right angle

size = 3
for row in range(0, size):     
    for space in range(0,row):
        print(" ",end="")    
    for column in range(0,size - row):
        print("q",end="")
    print()

# 3rd triangle top left right angle

size = 3
for row in range(0, size):       
    for column in range(0,size - row):
        print("o",end="")
    print()

# 4th triangle bottom right right angle

size = 3 
for row in range(1, size + 1): # 1
    for space in range(1, size - row + 1): # 2
        print(' ', end = '') # 3
    for column in range(1, row + 1): # 4
        print('*', end = '') # 5
    print() # 6



# Rebekahs triangles

size=3

for line in range (1, size+1):

    for space in range (1, line):

        print (' ', end='')

    for asterisk in range (1, size - line + 2):

        print ('*', end='')

    print()

 
# Rebekahs triangles

size=3

for line in range (1, size+1):

    for asterisk in range (1, size - line + 2):

        print ('*', end='')

    print()


    
