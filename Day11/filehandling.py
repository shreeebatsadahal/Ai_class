# f=open("file_namefullpath","mode-readedit")
# #file_name-sample.txt demo.docx
# #mode r:read w:write a:open

# data=f.read()
# f.close()

#creating a file
# file_path="newfile.txt"
# f=open(file_path,"x")  #x creates a new file
# print(f.name)
# print(f.mode)

#wrting something in the file
# f=open("newfile.txt","w")
# f.write(f"Hello we are trying file handling \n")
# f.write(f"This is interesting \n ")
# f.close()
# f=open("newfile.txt","r")
#data=f.read() #stores it as string whole file
# line1=f.readline()
# line2=f.readline()
# lines=f.readline()
# print(lines)
# print(line1)
# print(line2)


# #new method
# with open("newfile.txt","r") as f: #f is a variable
#  content=f.read()
#  print(content)

#  #to append something in the file 
# with open("newfile.txt","a") as f:
#     f.write("hello again")
     
 
#to copy the content from one file to another
#creating a new file 
# with open("newfile.txt","r") as f1:
#     content=f1.read()
# with open("note.txt","w") as f2:
#     f2.write(content)

