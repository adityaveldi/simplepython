# we will see how to take input from user using input()
name=input("Enter your name ")
# to ristrict the user to specific data we do as shown below.
age=int(input("Enter your age"))
#user can enter integer type as input for age variable.
if(age>=18):
    print("Hey", name,"your eligible for voting")

else:
    if(age>0 and age<18):
        calc=18-age
        print("sorry you have to wait more",calc,"year/years")



