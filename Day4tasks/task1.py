# Write the single line of code using and and not that sets a variable
# book_flight to True if (flight_cost is under the MAX_PRICE) AND (the
# destination is NOT "Asia").
# Output: Print the final boolean value of book_flight


a=input("Enter your destination: ")
b=float(input("Enter price of your ticket: "))
book_flight=b<80000 and not (a=='asia')
print(f"You can book flight: {book_flight}")