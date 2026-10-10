#WAP to print all numbers in a range divisible by a given number.
start=int(input("Enter the start number :"))
end=int(input("Enter the end number :"))
disvisor=int(input("Enter the number disvisor :"))
for i in range(start,end):
    if(i%disvisor==0):
        print("divisor by= ", i  ,"disvisor is :=",disvisor)