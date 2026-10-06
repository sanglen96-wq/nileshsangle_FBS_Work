age=int(input("Enter the age.. :"))
gender=str(input("Enter the gender:"))
if(age>=21):
    if(gender=='M'):
        print("you eligible for married")
    else:
        print("sorry you are not eligible for married")
else:
    if(age>=18):
        if(gender=='M'):
            print("you are eliglible for married")
    else:
        print("not eligilbe..")