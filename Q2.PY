#Write a program to input any alphabet and check whether
# it is vowel or consonant.

ch=str(input("Enter the your choice :"))
if ch.isalpha():
    print("this is the alphabet :",ch)
    if ch.lower() in"aeiou":
        print("is a vowel")
        
else:
    if ch.isdigit():
        print("this is the digit")
    else:
        print("Enter the valid...")
print("program is the sucessful....")