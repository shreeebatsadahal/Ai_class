# #1value error
# s=int("shree")
# print(s)


# #2type error
# a=45
# b='123'
# print(a+b)

# #3.zerodivisionerror
# a=45
# b=0
# print(a/0)

# # try:
# # risky code
# # except:
# #    fall back statement
# # finally:
# #  runs code anyhow error bhayeni nabhayeni

# try:
#     s=int("123")
#     print(s)
# except:
#     print("Exception occured")    
# finally:
#      print("code ended")

#4.index error
# list1=[12,"hello",45]
# try:
#    print(list1[3])
# except IndexError:
#    print("Index is out range")  

list1=["123","45","34","hello","python","100"]
#Convert the each element of the list to integer if compatabile other wise replace the incompatible element with the word INVALID
converted=[]
for element in list1:
    try:
        converted.append(int(element))
    except ValueError:
         converted.append("Invalid")     

print(converted)     
  
