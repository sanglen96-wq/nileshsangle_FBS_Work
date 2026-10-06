#Write a program to input angles of a 
# triangle and check whether triangle is valid or not.
angle1=int(input("Enter the angle 1 :"))
angle2=int(input("Enter the angle 2 :"))
angle3=int(input("Enter the angle 3 :"))

if angle1=='60':
    if angle2=='60':
        if angle3=='60':
            print("this is the triangle..")
else:
    print("not a triangle...")
    print("Enter the valid..")
            
