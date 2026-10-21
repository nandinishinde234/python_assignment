age = int(input("Enter your age: "))
test_passed = input("Have you passed the driving test? (yes/no): ")

if age >= 18:
    if test_passed.lower() == "yes":
        print("Person is eligible for a driving license.")
    else:
        print("Person is not eligible because the driving test is not passed.")
else:
    print("Person is not eligible because the age is below 18.")