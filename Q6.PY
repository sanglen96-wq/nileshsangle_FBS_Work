#Write a program to check if user has entered correct userid and password.

userid=str(input("Enter the userid..."))
password=int(input("Enter the password."))

if(userid=='ABC'):
    if(password==123):
        print("correct user id and password..")
else:
    print("please enter the valid..not correct")