#
# Madison Blake
# 09-23-2024
# Bug Collector Programming Project
# COSC 2409 DNT
#
# Initialize variables for bugs and total number of bugs collected.
def main():
    try:
        total = int(input("Enter total cost of items? "))
        num_items = int(input("Number of items "))
        average = total / num_items
    except ZeroDivisionError:
        print('ERROR: cannot have 0 items')
    except ValueError:
        print('ERROR: number of items cannot be negative')
main()