password = input("Enter password: ")

if len(password) >= 8:
    if password == "Python@123":
        print("Password is valid.")
    else:
        print("Incorrect password.")
else:
    print("Password must contain at least 8 characters.")