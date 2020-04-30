
# Dairy farm produces 1234 litres of milk per day
# It puts them in 4 pint (2.27 litre) bottles
# How many bottles are completely filled each day

milk = 1234
litre = 2.27

total_bottles = milk/litre
whole_bottles = milk//litre
remain_bottles = milk%litre

print(total_bottles)
print(whole_bottles)
print(remain_bottles)

# Volume of a brick

length = 3
width = 2
height = 4

volume = length * width * height

print('The volume is', volume)


# How many photos of 13MB each will fit in a 1000MB disk?

photo = 13
disk = 1000

photo_in_disk = disk//photo

print(photo_in_disk, 'photos of', photo, 'MB fit in', disk, 'MB')

# Calculate restaurant bill

bill = 10
charge = 1
people = 10

if people <= 6:
    total = bill
else:
    total = bill + (bill * charge)

print('The total bill is', total)

# given the marks obtained by a student, print the students grade

mark = 80

if mark < 40:
    grade = 'fail'
elif mark <= 60:
    grade = 'pass'
elif mark < 80:
    grade = 'merit'
else: # mark >= 80:
    grade = 'distinction'

print('The grade is a', grade)

# Given initial mortgage, annual interest rate, and mthly payment amount
# Print outstanding mortage, month by month until is is paid off


rate = 0.05
payment = 200
mortgage = 1000

print('Outstanding mortgage:', mortgage)
while (mortgage > 0):
    interest = mortgage * (rate/12)
    mortgage = mortgage + interest - payment
    print('Outstanding mortgage:', mortgage)

# Given the Richter magnitude, print a message

magnitude = 8

if magnitude < 4:
    description = 'minor'
elif magnitude < 6:
    description = 'moderate'
elif magnitude < 7:
    description = 'strong'
elif magnitude < 8:
    description = 'major'
else:
    description = 'great'
    
print('That is a', description, 'earthquake')

# While loop

A = 9
B = 5
C = 8

seed = 3
print(seed)

result = ((seed * A) + B) % C
print(result)


while not (result == seed):
    result = ((result * A) + B) % C
    print(result)
   
               
