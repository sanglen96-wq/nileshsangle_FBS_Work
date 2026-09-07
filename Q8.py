#WAP a program to convert the day into years,week and days

day=int(input("Enter the days :"))
years=(day//365)
remainingday=(day%365)
week=remainingday//7
days=remainingday%7

print("years are :",years)
print("remaingdays",remainingday)
print("week are",week)
print("days are ",day)