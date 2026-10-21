role = input("Enter user role (admin/user/guest): ").lower()

match role:
    case "admin":
        print("Welcome Admin! You have full access.")
    case "user":
        print("Welcome User! You have normal access.")
    case "guest":
        print("Welcome Guest! You have limited access.")
    case _:
        print("Invalid user role.")