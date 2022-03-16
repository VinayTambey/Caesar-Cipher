import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
user_letter = int(input("How many letters would you like in your password?\n"))
user_symbols = int(input("How many symbols would you like?\n"))
user_num = int(input("How many numbers would you like?\n"))

# EASY
# passwords = ""
# for l in range(1, user_letter + 1):
#     passwords += random.choice(letters)
#
# for s in range(1, user_symbols + 1):
#     passwords += random.choice(symbols)
#
# for n in range(1, user_num + 1):
#     passwords += random.choice(numbers)

# print(passwords)

 # HARD
passwords = []
for l in range(1, user_letter + 1):
    passwords.append(random.choice(letters))

for s in range(1, user_symbols + 1):
    passwords.append(random.choice(symbols))

for n in range(1, user_num + 1):
    passwords.append(random.choice(numbers))

random.shuffle(passwords)

password = ""
for num_char in passwords:
    password += num_char
print(f"Your password is: {password}")

