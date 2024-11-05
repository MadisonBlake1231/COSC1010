#
# Madison Blake
# 11-04-2024
# Exception Handling Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Open file
loop_count = 0
total = 0
data = open("numbers.txt","r")

# Handle IOError
try:
    f = open('numbers.txt', 'r')
    content = f.read()
    f.close()
except IOError:
    print('File not found.')

# Read data
for line in data.readlines():
    # Calculate average
    total = total + int(line)
    loop_count += 1
avg = total/loop_count

# Handle ValueError
try:
    data = int
except ValueError:
    print("Data is invalid.")

# Display average
print (avg)