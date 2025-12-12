import string
import random

choices = ['y' , 'n']
include_letter = None
include_number = None
include_symbol = None

while True:

  pw_length_input = input("Enter password length between 12 and 20 (numeric only): ")

  if pw_length_input.isdigit() and 12 <= int(pw_length_input) <= 20:
    
    pw_length = int(pw_length_input)
    print(f"Password length set to: {pw_length_input}")
    break
  
  else:

    print("Invalid input.")

while include_letter not in choices:
  
  include_letter = input("Do you want your password to include letters ? (Y/N): ").lower()

while include_number not in choices:
  
  include_number = input("Do you want your password to include numbers ? (Y/N): ").lower()

while include_symbol not in choices:
  
  include_symbol = input("Do you want your password to include symbols ? (Y/N): ").lower()


pwcharacters = []

if include_letter == 'y':
  
  pwcharacters += string.ascii_letters

if include_number == 'y':
  
  pwcharacters += string.digits

if include_symbol == 'y':
  
  pwcharacters += string.punctuation

if not pwcharacters:
  
  print("Not enough characters to create password.")

else:
  
  password = ''.join(random.choice(pwcharacters) for character in range(pw_length))
  print("Generated password:", password)
