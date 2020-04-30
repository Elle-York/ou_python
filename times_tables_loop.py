# Times Table
# -------------------------------------------------------------
# Produce a times table showing all possible multiplications of 1 to 12 in order
# Show all multiples of 1
# Show all multiples of 2 etc.
# see page 113 - part 2 - activity 2.18

size = 4
for row in range (1, size + 1):
    for column in range(1, size + 1):
        print(row * column, end= ' ')  # when we don't want print to move to a new line, use end=, this appends a space on the line
    print() # If this is indented by one step, it changes it to a column!
                
