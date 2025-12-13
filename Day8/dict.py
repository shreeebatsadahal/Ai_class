#dictionary
dict1={} #empty dictonary
print(type(dict1))
dict2={"key1":"value1",
       "key2":"value2",
       "key3":"value3"}
dict3={"name":"shree",
      "roll no":"813036",
      "address":"brt",
      "marks":[45,46,48,49]} #value can be list
print(dict3)
print(list(dict3.keys()) )#prints all the keys in dictionary
print(dict3.values()) #prints all the values in dictionary
#key should be unique in dictionary if we give same key again it will overwrite the previous value;value can be duplicate
print(list(dict3.items())) #prints all the key value pairs in dictionary

for i in dict3.keys():
    print(i) #prints all the keys in dictionary
for i in dict3.values():
    print(i) #prints all the values in dictionary
print(dict3["address"])

for i in dict3.items():
    print(i) #prints all the key value pairs in dictionary

dict3["address"]="kathmandu" #to change value of key
print(dict3)
dict3.update({"roll no":"813037"}) #another way to change value of key
print(dict3)

for i,j in dict3.items():
    print(f"{i}:{j}") 