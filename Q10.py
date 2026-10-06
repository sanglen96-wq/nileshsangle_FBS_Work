'''Question: Accept age of five people and ticket amount per person, then calculate the total ticket amount:

Children below 12 → 30% discount
Senior citizens above 59 → 50% discount
Others → Full amount'''

total=0
for i in range(5):
    age=int(input("Enter the age :"))
    ticket=float(input("Enter the ticket amount :"))
    if age<12:
     amount=ticket-(ticket*30/100)
    elif(age<12):
        amount=ticket-(ticket*30/100)
    elif age>59:
        amount=ticket-(ticket*30/100)
    else:
        amount=ticket
    total=total+amount
print("total ticket amount =",total)    