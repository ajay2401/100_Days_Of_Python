import random

numbers = list("123456789")

alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

alpha_count = int(input("\nenter number of alphabets you want in your password\n"))
symbol_count = int(input("\nenter number of symbols you want in your password\n"))
num_count = int(input("\nenter number of numbers you want in your password\n"))

# ********************************************************
#                  Easy Case
# ********************************************************

easy_pwd = ""

for counter in range(0,alpha_count):
    easy_pwd = easy_pwd + random.choice(alphabets)

for counter in range(0,symbol_count):
    easy_pwd = easy_pwd + random.choice(symbols)    

for counter in range(0,num_count):
    easy_pwd = easy_pwd + random.choice(numbers)

print(f"Your easy case password is: {easy_pwd}")

# ********************************************************
#                  Hard Case
# ********************************************************

hard_pwd_list = list(easy_pwd)

random.shuffle(hard_pwd_list)

print(f"Your hard case password is: {''.join(hard_pwd_list)}")

# ********************************************************
#                  Harderrrr Case
# ********************************************************

hard_pwd_src = numbers + alphabets + symbols

hard_pwd_output = ""

for index in range(0,random.randint(10,16)):
    hard_pwd_output = hard_pwd_output + random.choice(hard_pwd_src)

print(f"Your harederr case password is: {hard_pwd_output}")