# set={} #it is not a empty set it is a dictionary
# print(type(set))
set1=set()
print(type(set1))
set2={1,2,3,4,5,6,7,8,9}
print(type(set2))
print(set2)
#there is no indexing in set 
set3={1,2,3,4,5,5,5,5,5,5} #it will print only unique values
set4={1,2,3,4,5}
set5=(2,4,7,8,9)
print(set4.difference(set5))
print(set4.union(set5))
print(set4.intersection(set5))
print(set4.issubset(set5))
print(set4.isdisjoint(set5))
print(set4.intersection_update(set5))
# print(set4 + set5) #you can add two sets using + operator
set6={1,2,3,4,5}
print (set6)
set6.add(6)
print(set6)
#set is mutable element is immutable meaning you can add or remove element but you cant change value of element
set={1,2,3,(4,5,6),10}
print(set)
print(type(set))
# set={1,2,3,[4,5,6],10} #this is nt valid coz list is mutable and set cant have mutable element
