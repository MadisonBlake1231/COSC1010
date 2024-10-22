#
# Madison Blake
# 10-21-2024
# File Display Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program.    

def main():
    
    # Declare local variables
    contents = ''
    # Open the numbers.txt file for reading.
    infile = open('numbers.txt', 'r')
    
    # Read and display the file's contents.
    contents = infile.read()

    # Print contents
    print(contents)

# Call the main function
main()