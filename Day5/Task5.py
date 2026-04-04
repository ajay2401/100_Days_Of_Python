import random

numbers = [1,2,3,4,5,6,7,8,9]

sum_of_numbers = sum(numbers)
print(f"\nThe sum of numbers is: {sum_of_numbers}\n")

max_of_numbers = max(numbers)
print(f"\nThe maximum of numbers is: {max_of_numbers}\n")

x = random.choice(range(10,15))
print(x)

# Find max

max_value = 0

for index in numbers:
    if max_value > index:
        max_value = index

print(f"Maximum value is: {max_value}\n")

for i in range(1,5):
    print(i)

for j in range(1,5,1):
    print(j)

