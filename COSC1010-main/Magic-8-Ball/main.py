#
# Madison Blake
# 11-04-2024
# Magic 8 Ball Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Import Random module
import random
# Define number parameters
numbers = []
numbers 
for count in range (7):
    numbers.append (random.randint (0,9))
# Display list of chosen numbers
import random
    # Define Range
MAX_DIGITS = 7  # Max number of digits
START = 0   # Start of range
END = 9     # End of range
# Main function
def main ():
    # Create a list.
    numbers = [0]*7
    # Populate the list with random numbers.
    for index in range(MAX_DIGITS):
        numbers[index] = random.randint (START, END)
    # Display random numbers
    print ('Here are your lottery numbers:')
    for index in range (MAX_DIGITS):
        print(numbers[index], end='')
    print()
main ()