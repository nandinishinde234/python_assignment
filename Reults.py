result = input("Enter result status (pass/fail): ").lower()

match result:
    case "pass":
        print("Congratulations! You passed.")
    case "fail":
        print("Sorry! You failed.")
    case _:
        print("Invalid result status.")