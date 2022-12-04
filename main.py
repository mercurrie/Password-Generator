import random

# Create list of letters, symbols, and numbers
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Retrieve usr inputs

user_letters = int(input("How many letters would you like in your password?\n")) 
user_symbols = int(input(f"How many symbols would you like?\n"))
user_numbers = int(input(f"How many numbers would you like?\n"))

# Create empty list to hold password
passwordList = []

# Add letters to list
for letter in range(1, user_letters + 1 ):
    passwordList.append(random.choice(letters))
# Add symbols to list
for symbol in range(1, user_symbols + 1 ):
    passwordList.append(random.choice(symbols))
# Add numbers to list
for number in range(1, user_numbers + 1):
    passwordList.append(random.choice(numbers))
    

# Shuffle contents of list
random.shuffle(passwordList)

password = ""

# Create string from list content
for i in passwordList:
    password += i
    
print(f'Your generated password is: {password}')