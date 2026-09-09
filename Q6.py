#WAP to calculate total salary of employee 
# based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.
basic=float(input("Enter the basic salary :"))
da=(basic*10)/100
ta=(basic*12)/100
hra=(basic*15)/100
tota_salary=(basic+da+ta+hra)

print("da salary",da)
print("ta salary",ta)
print("hra salary",hra)
print("total_salary :",tota_salary)