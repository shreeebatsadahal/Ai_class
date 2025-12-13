#program to calculate the total to be paid of several units of items after deducting discount and adding tax
a=int(input("Enter the number of items you bought" ))
b=float(input("Enter the price per item: "))
total=a*b
print(f"The total price before discount and tax is:{total}")
print("The fixed discount is 20%")
total *=0.8
print(f"The total price after discount is:{total}")
print("The tax rate is 13%")
total *=1.13   
print(f"The total price of {a}items at the rate of {b} per item after discount and tax is:{total}")
