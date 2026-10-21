age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

if age >= 18 and weight >= 50:
    print("Eligible for blood donation")
else:
    print("Not eligible for blood donation")