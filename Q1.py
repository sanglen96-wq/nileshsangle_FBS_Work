#convert the time entered in hh,min,second,into second 

hh=int(input("Enter the hh :"))
min=int(input("Enter the min :"))
sec=int(input("Enter the sec :"))
total_sec=(min*60)+(hh*3600)+sec
print(f"total second are {total_sec}")