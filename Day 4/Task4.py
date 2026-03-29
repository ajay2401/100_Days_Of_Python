import random

random_integer = random.randint(1,10)
print(random_integer)

random_floating = random.random() * 2
print(random_floating)

random_uniform_floating = random.uniform(1,2)
print(random_uniform_floating)

list = ["John","Alice","Alex","David","Mark"]
print("The person to pay is: " + random.choice(list))