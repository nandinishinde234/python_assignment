amount = float(input("Enter total shopping amount: "))

if amount >= 5000:
    discount = amount * 20 / 100
elif amount >= 3000:
    discount = amount * 15 / 100
elif amount >= 1000:
    discount = amount * 10 / 100
else:
    discount = 0

final_amount = amount - discount

print("Discount is:", discount)
print("Final amount is:", final_amount)