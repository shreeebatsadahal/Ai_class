def sum(a,b):
    add=a+b
    return a+b,a-b,a*b,a/b
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
result=sum(a,b)
a,b,c,d=result
print("Sum is:",a)
print("Difference is:",b)
print("Product is:",c)
print("Quotient is:",d)


def sum(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
result=sum(a,b)
print("Sum is:",result[0])
print("Difference is:",result[1])
print("Product is:",result[2])
print("Quotient is:",result[3])
