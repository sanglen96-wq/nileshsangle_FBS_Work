#WAP to calculate and sum of three-digit

num=int(input("Enter the num :"))
a=num//100
b=(num//10)%10
c=(num%10)
sum=a+b+c
print("sum of three digit :",sum)