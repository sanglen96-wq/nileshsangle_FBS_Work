#10. WAP to check if given number is Perfect Number.
num = int(input("Enter the number: "))
total = 0

for i in range(1, num):
    if num % i == 0:
        total = total + i

if total == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")