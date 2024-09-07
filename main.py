#
# Madison Blake
# 09/06/2024
# Sales Prediction Programming Project
# COSC 2409 DNT
#

# Variables to hold the sales total and the profit
total_sales = 0

# Get the amount of projected sales.
total_sales = float (input('Enter the projected sales: '))

# Calculate the projected profit as 23 precent of total sales.
profit = total_sales * 0.23

# Print the projected profit.
print('The profit is $', format(profit, ',.2f'))
