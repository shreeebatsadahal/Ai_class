#prepare the file to store the grade and scores of the student by calculating percentage and grade    
def calculate_score():
    phy=float(input("ENter your marks"))
    chem=float(input("enter your chem marks"))
    math=float(input("ENter your marks"))
    percentage=(phy+math+chem)/3
    return phy,chem,math,percentage
def calculate_grade(percentage):
    if percentage>90:
        print("A+ grade")
    elif percentage>80:
        print("A grade")
    elif percentage>70:
        print("B+ grade")
    elif percentage>60:
        print("B grade") 
    elif percentage>50:
        print("C+ grade") 
    elif percentage>40:
        print("C grade")
    else:
        print("FAIL cant calculate your grade")
def main():
    name=input("Enter the name of student")
    rollno=input("ENter the roll no:")
    phy,chem,math,score=calculate_score()  
    grade=calculate_grade(score)                          
    with open("student.txt","a") as f:
        f.write(f"-----RESULT----- \n")
        f.write(f"Name={name} \n")
        f.write(f"Name={rollno} \n")
        f.write("----MARKS---- \n")
        f.write(f"phy:{phy} \n")
        f.write(f"chem:{chem} \n")
        f.write(f"math:{math} \n")
        f.write("----FINAl Score----\n")
        f.write(f"percentage{score}")

main()      