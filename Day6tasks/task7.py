#  Take a number as input and print its multiplication table up to 10. (Assignment)
a=int(input("Enter a number"))
for i in range(1,11):
    print(f"{a}*{i}={a*i}")
