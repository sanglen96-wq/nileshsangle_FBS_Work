#Question 6: WAP to check if a given number is prime or not.

number=int(input("Enter the number :"))

if number<=1:
    print("not prime")
else:
    for i in range(2,number):
        if number % i==0:
            print("not prime")
            break
        else:
            print("are the prime number",number)