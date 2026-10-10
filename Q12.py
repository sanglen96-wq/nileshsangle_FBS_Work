#12. Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
#4*4*4*4)

num = int(input("Enter the number: "))

temp = num
count = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** count
    temp = temp // 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")