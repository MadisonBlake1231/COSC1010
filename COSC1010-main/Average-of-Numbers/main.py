#
# Madison Blake
# 10-21-2024
# Average of Numbers Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Open file
loop_count = 0
total = 0 
data = open("numbers.txt", "r")

# Read data
for line in data.readlines():

    # Calculate average
    total = total + int(line)
    loop_count += 1
avg = total/loop_count

# Display average
print(avg)