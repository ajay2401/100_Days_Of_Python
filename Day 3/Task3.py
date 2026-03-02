height = 122

if height > 120:
    print("Tall enough\n")
else:
    print("Drink Milk and get Taller\n")

number  = input("Enter the number to check\n")

if(int(number) == 0):
    print("Enter a value more than zero\n")
elif(int(number) % 2 == 0):
    print(f"{number} is an even number\n")
else:
    print(f"{number} is an odd number\n")

