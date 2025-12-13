#creating a file safely
try:
    with open("file.txt", "x") as f:
        print(f.name, f.mode)
        # x makes a file 
except FileExistsError:
    print("file.txt already exists, skipping creation.")

with open("file.txt", "w") as f:
    f.write("This is a new file created by me")
    f.write("\nThis is the second line of the file")

#if i AGAIN OPEN IT AND WRITE WITH MODE W IT WILL OVERWRITE THE FILE BUT IF I OPEN AGAIN AND USE APPENDED IT WILL ADD FROM LAST    
with open("file.txt", "a") as f:
    f.write("\nThis is the appended line of the file")
    f.write("\nThis is the fourth line of the file")
#reading the file
with open("file.txt", "r") as f:  
    #you need a variable to read the file
    data=f.read()
    print(data) 

#reading a binary file


# with open("binary_file","rb") as f:
    #rb is read binary
    #binary_file is a file that contains binary data like img.jpg etc


with open("C:\\Users\\Asus\\Downloads\\photo.jpg","rb") as f:
    data=f.read()
    print(data)  #this will print the binary data of the image file

with open("copyimg.jpg","wb") as f:
    f.write(data)  #this will write the binary data to a new file called copyimg.jpg
 