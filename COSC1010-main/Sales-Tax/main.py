#
# Madison Blake
# 09/06/2024
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations
purchase = 0.0
stateTax = 0.0
countryTax = 0.0
totalTax = 0.0
totalSale = 0.0

# Constants for the state and county tax rates
STATE_TAX_RATE = 0.05
COUNTRY_TAX_RATE = 0.025

# Get the amount of the purchase.
purchase = float(input("Enter the amount of the purchase: "))

# Calculate the state sales tax.
stateTax = purchase * STATE_TAX_RATE

# Calculate the county sales tax.
countryTax = purchase * COUNTRY_TAX_RATE

# Calculate the total tax.
totalTax = stateTax + countryTax

# Calculate the total of the sale.
totalSale = purchase + totalTax

# Print information about the sale.
print("Purchase Amount:", format(purchase, '.2f'))
print("State Tax:", format(stateTax, '.2f'))
print("Country Tax:", format(countryTax, '.2f'))
print("Total Tax:", format(totalTax, '.2f'))
print("Sale Total:", format(totalSale, '.2f'))