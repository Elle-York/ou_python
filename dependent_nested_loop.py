# 1 Print right-angled triangle
size = 3
for line in range(1, size + 1):
    for asterisk in range(1, line + 1): 
        print(' * ', end = '  ')
    print()

# 2 Print equilateral triangle in the opp direction
size = 3
for line in range(1, size + 1):
    for space in range(1, size - line + 1):
        print('  ', end = ' ')
    for asterisk in range(1, line + 1): 
        print(' * ', end = '  ')
    print()

# 3 And another style...
size = 3
for line in range(1, size + 1):
    for asterisk in range(1,  size - line + 2): 
        print(' * ', end = '  ')
    print()


# 4 Print  triangle in the opp direction
size = 3
for line in range(1, size + 1):
    for asterisk in range(1, size - line + 1): 
        print(' * ', end = '  ')
    print()

# 5 Expermenting

size = 3
for line in range(3):
    for space in range(10, 20):
        print('  ', end = ' ')
    for asterisk in range(1, line - 1): 
        print(' x', end = '  ')
    print()


