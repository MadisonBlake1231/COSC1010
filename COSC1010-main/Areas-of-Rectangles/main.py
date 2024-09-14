#
# Madison Blake
# 09/14/2024
# Areas of Rectangles Programming Project
# COSC 2409 DNT
#
# Local variables
length1 = 0
width1 = 0
length2 = 0
width2 = 0
area1 = 0
area2 = 0

# Get length A
length1 = int(input('Enter the length of rectangle 1: '))

# Get width A
width1 = int(input('Enter the width of rectangle 1: '))

# Get length B
length2 = int(input('Enter the length of rectangle 2: '))

# Get width B
width2 = int(input('Enter the width of rectangle 2: '))

# Calculate area A
area1 = length1 * width1

# Calculate area B
area2 = length2 * width2

# Print area comparison using if-elif-else statements
if area1 > area2:
    print ('Rectangle 1 has the greatest area. ') 
elif area2 > area1:
    print('Rectangle 2 has the greatest area. ')
else:
    print('Both rectangles have the same area.')