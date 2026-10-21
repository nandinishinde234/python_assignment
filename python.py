print("----- Language Menu -----")
print("1. Python")
print("2. Java")
print("3. C")
print("4. C++")

choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print("You selected Python")
    case 2:
        print("You selected Java")
    case 3:
        print("You selected C")
    case 4:
        print("You selected C++")
    case _:
        print("Invalid choice")