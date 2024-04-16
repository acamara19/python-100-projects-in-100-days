"""
A Password Generator Program
"""
import random

print("Welcome to the PyPassword Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_letters = int(input("How many letters would you like in your password? "))
password_symbols = int(input("How many symbols would you like in your password? "))
password_numbers = int(input("How many numbers would you like in your password? "))

password_list = []

for char in range(1, (password_letters + 1)):
    password_list.append(random.choice(letters))

for char in range(1, (password_symbols + 1)):
    password_list += random.choice(symbols)

for char in range(1, (password_numbers + 1)):
    password_list += random.choice(numbers)

random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char
print("-----------------------------------------------------")
print(f"Your password is: {password}")
