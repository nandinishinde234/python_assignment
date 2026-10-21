salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years >= 5:
    bonus = salary * 10 / 100
    print("Bonus is:", bonus)
else:
    print("No bonus")