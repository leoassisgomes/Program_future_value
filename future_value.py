# P = F
#----------- 
# (1 + r)n


# Here is the algorithm:

# 1. Get the desired future value.
# 2. Get the annual interest rate.
# 3. Get the number of years that the money will sit in the account
# 4. Calculate the amount that will have to be deposited
# 5. Display the result of the calculation in step 4


# Get the desired future value.

future_value = float(input('Enter the desired future value: '))

# Get the annual interest rate

rate = float(input('Enter the annual interest rate: '))

# Get the number of years that the money will appreciate.

years = int(input('Enter the number of years the money will grow: '))

# Calculate the amount needed to deposit.
present_value = future_value / (1.0 + rate) ** years

# Display the amount needed to deposit.
print('You will need to deposit this amount: ', present_value)
