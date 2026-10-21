num = int(input("Enter a number: "))

if num % 3 == 0:
    if num % 5 == 0:
        print("The number is divisible by both 3 and 5.")
    else:
        print("The number is divisible by 3 but not by 5.")
else:
    print("The number is not divisible by 3.")