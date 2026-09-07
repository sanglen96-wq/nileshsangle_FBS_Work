#WAP to calculate the compound interest

p=float(input("Enter the principle :"))
r=float(input("Enter the rate :"))
t=float(input("Enter the time :"))

amount=p*(1+r/100)**t
ci=amount-p
print(f"amount is :{amount}")
print(f"compound interest is :{ci}")
