year = int(input("Enter a year: "))

if year % 100 == 0:
    print("It is a century year.")

    if year % 400 == 0:
        print("It is also a leap year.")
    else:
        print("It is not a leap year.")
else:
    if year % 4 == 0:
        print("It is a leap year.")
    else:
        print("It is not a leap year.")