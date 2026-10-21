age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: "))

if age >= 21:
    if salary >= 25000:
        print("Person is eligible to apply for the loan.")
    else:
        print("Person is not eligible due to low salary.")
else:
    print("Person is not eligible due to age.")