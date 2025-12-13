#list(mutable arrays),tuples(immutable),dictionaries (hashtables) and sets these are built in datastructure
list1=[1,True,3,"shree",5.37] #we can put heterogenous data type in list
print(type(list1))
print(list1)
list2=[1,2,3,4,5]
print(type(list2))
print(list2)
list2[3]="java"
print(list2)
#emptylist
emptylist=[]
print(emptylist)
empty_list=list()
print(empty_list)
#how to insert data in empty list
emptylist.append("hello")
emptylist.insert(0,"list")
print(emptylist)
#listname.remove('value) it removes value from the list
#listname.extend([value1,value2]) extend function helps to add multiple values
list3=[1,2,3,4,5]
list3.extend([55,6])
print(list3)

for i in list3:
    print(i)
print(list3[2:3]) 
print(len(list3))  #gives length of list
#list3[2:3] gives the value of index 2 to 3 but not including 3