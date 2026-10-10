#8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

start=int(input("Enter the start number :"))
end=int(input("Enter the end number :"))
for i in range(start,end+1):
    if(i%5==0 and i%7==0):
        print("this are the number divisible by the 5 and 7",i)