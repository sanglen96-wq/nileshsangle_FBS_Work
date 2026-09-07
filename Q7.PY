
#WAP to calculate root of quadric equation
import math
a=float(input("Enter the a :"))
b=float(input("Enter the b:"))
c=float(input("Enter the c:"))

d=b*b-4*a*c
sqrt_d=math.sqrt(d)
root1=(-b+sqrt_d)/(2*a)
root2=(-b - sqrt_d)/(2*a)

print("root 1:",root1)
print("root 2:",root2)