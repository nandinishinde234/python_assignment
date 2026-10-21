print("----- ATM MENU -----")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print("Your balance is ₹10,000")
    case 2:
        print("Deposit option selected")
    case 3:
        print("Withdraw option selected")
    case 4:
        print("Thank you for using the ATM")
    case _:
        print("Invalid choice")