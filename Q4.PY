#Write a program to check whether the triangle is 
# equilateral, isosceles or scalene triangle.

side1=int(input("Enter the side1 :"))
side2=int(input("Enter the side 2 :"))
side3=int(input("Enter the side 3 :"))

if (side1==side2==side3):
    print("this is the Equilateral...")
else:
    if(side1==side2):
        if(side2==side3):
            if(side1==side3):
                print("isoceles")
print("scalene")