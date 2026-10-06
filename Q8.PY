m1=int(input("Enter the marks m1 :"))
m2=int(input("Enter the marks m2:"))
m3=int(input("Enter the marks m3 :"))
m4=int(input("Enter the marks m4:"))
m5=int(input("Enter the marks m5:"))
total=m1+m2+m3+m4+m5/5
percentage=total/5
print("percentage...",percentage)
if percentage>=75:
    print("Good marks ",percentage)
elif(percentage>=60):
    print("first class")
elif(percentage>=50):
    print("second class")
elif(percentage>=35):
    print("pass")
else:
    print("sorry you are fail...")