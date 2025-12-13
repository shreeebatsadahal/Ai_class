#ask the user to enter the 5 numbers and create the list
number_list=[]
count=0
while count<5:
    n=int(input("Enter a number: "))
    number_list.append(n)
    count+=1
print("The list of numbers is:", number_list)

list=[]
#for loop: create a list of 5 numbers then store its squares in another list
for i in range(5):
    n=int(input("Enter a number: "))
    list.append(n)
print("The list of numbers is:", list)
squared_list=[]
for i in list:

    squared_list.append(i**2)
print("The list of squares is:", squared_list)

#explore all the methods of list,tuples,sets and dictionaries
