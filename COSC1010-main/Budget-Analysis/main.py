#
# Madison Blake
# 09-23-2024
# Budget Analysis Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

while True:
    month = 0 
    total_real = 0
    total_est = 0
    

    # Rent Projected vs Rent Actual
    print('Projected rent')
    rent_p = float(input())
    total_est += rent_p
    print('Actual rent')
    rent_a = float(input())
    total_real += rent_a

    # Debt Projected vs Debt Actual
    print('Projected debt')
    debt_p = float(input())
    total_est += debt_p
    print('Actual debt')
    debt_a = float(input())
    total_real += debt_a

    # Gas Projected vs Gas Actual
    print('Projected gas')
    gas_p = float(input())
    total_est += gas_p
    print('Actual gas')
    gas_a = float(input())
    total_real += gas_a

    # Food Projected vs Food Actual
    print('Projected food')
    food_p = float(input())
    total_est += food_p
    print('Actual food')
    food_a = float(input())
    total_real += food_a

    # Insurance Projected vs Insurance Actual
    print('Projected insurance')
    insurance_p =float(input())
    total_est += insurance_p
    print('Actual insurance')
    insurance_a = float(input())
    total_real += insurance_a

    # Utilities Projected vs Utilities Actual
    print('Projected utilities')
    utilities_p =float(input())
    total_est += utilities_p
    print('Actual utilities')
    utilities_a = float(input())
    total_real += utilities_a

    if total_real > total_est:
        #Over Budget
        print('You are over budget by: ' ,total_real - total_est)
    elif total_est > total_real:
        #Under Budget
        print('You are under budget by: ' , total_est - total_real)
    else:
        #Exact Budget
        print('You are exactly on budget! You spent: ' , total_real)
    print('---------- New Month -----------')