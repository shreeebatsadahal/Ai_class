# balance = 1000.00
# deposit = 250.00
# service_fee = 10.50
# interest_rate = 1.05 ( 5% growth)
# 3. Question: Perform the following operations using assignment operators:
# 1.Apply the deposit using the += operator.
# 2.Subtract the service_fee using the -= operator.
# 3.Apply the interest_rate multiplier (for growth) using the *= operator.
# 4.Initialize a new variable, shares, with the final balance. Then, use the //=
# operator on shares to determine how many full $100 units (shares) can be
# purchased from that amount.
# Output: Print the balance after steps 1, 2, and 3, and the final integer value of
# shares after step 4.

balance=1000.00
print(f"Your Balance is: {balance}")
balance +=250
print(f"Your new balance after deposit is: {balance}")
balance -=10.50
print(f"Your new balance after service fee deduction is: {balance}")
balance *=1.05
print(f"Your balance after interest is: {balance}")
shares=balance
shares //=100
print(f"You can purchase {shares} full $100 units (shares) from your balance.")
