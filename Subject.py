# Check whether a student passed all subjects

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

if maths >= 40 and science >= 40 and english >= 40:
    print("Student passed all subjects.")
else:
    print("Student failed in one or more subjects.")