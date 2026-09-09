#Write a program to swap two numbers without using third variable.
a=int(input("Enter the a values :"))
b=int(input("Enter the b values :"))

temp=a
a=b
b=temp

print("a :",a)
print("b :",b)