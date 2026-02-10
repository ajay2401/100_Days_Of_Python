print("\n" + "Welcome to the TIP Calculator" + "\n")

bill_value = float(input("Please enter the total amount of the bill\n $"))

tip_percent = float(input("Please enter the tip percentage\n"))

member_count = int(input("Please enter the number of ppl to split the bill with\n"))

final_share = round(((tip_percent / 100 * bill_value) + bill_value) / member_count, 2)

print(f"Each person should pay: ${final_share}")

