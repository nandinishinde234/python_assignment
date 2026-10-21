num = int(input("Enter a number: "))

if num >= 0 and num <= 9:
    print("Single digit number")
elif num >= 10 and num <= 99:
    print("Double digit number")
elif num >= 100 and num <= 999:
    print("Three digit number")
else:
    print("Number is more than three digits")