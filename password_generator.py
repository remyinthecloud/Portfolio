#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('''Welcome to the JuiceBox Password Generator!\nIt is an honor to be securing your data throughout the web :)''')
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

passwords = []

if nr_letters > 0:
  for letter in range(0, nr_letters):
    rand_letter = random.choice(letters)
    passwords.append(rand_letter)
else:
  print('\nInvalid number of characters.')
    
if nr_symbols > 0:
  for symbol in range(0, nr_symbols):
    rand_symbol = random.choice(symbols)
    passwords.append(rand_symbol)
else:
  print("\nInvalid number of symbols")
    
if nr_numbers > 0:
  for number in range(0, nr_numbers):
      rand_number = random.choice(numbers)
      passwords.append(rand_number)
else:
  print("\nInvalid number of numbers")

random.shuffle(passwords)
print("Here is your password: ", *passwords, sep='')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P