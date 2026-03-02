print("\n*** Pizza Delivery Python Program ***\n")

size = input("Enter the size of the Pizza - S / M / L\n")

pineapple = input("Do you want pineapple toppings? Y /N\n")

cheese = input("Do you really want more cheese? Y / N\n")


if size == 'S':
    bill = 15
    if pineapple == 'Y':
        bill += 2
    if cheese == 'Y':
        bill += 1
elif size == 'M':
    bill = 20
    if pineapple == 'Y':
        bill += 3
    if cheese == 'Y':
        bill += 1
elif size == 'L':
    bill = 25
    if pineapple == 'Y':
        bill += 3
    if cheese == 'Y':
        bill += 1

print(f"Your final bill amount is: ${bill}")