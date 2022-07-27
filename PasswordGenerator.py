import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

newArr = []
password = ""

for letter in range(0,nr_letters):
  password_letter = letters[random.randint(0,len(letters)-1)]
  newArr.append(password_letter)
  
for symbor in range(0,nr_symbols):
  password_symbol = symbols[random.randint(0,len(symbols)-1)]
  newArr.append(password_symbol)
  
for number in range(0,nr_numbers):
  password_number = numbers[random.randint(0,len(numbers)-1)]
  newArr.append(password_number)

list = range(0,len(newArr))
random_index = random.sample(list,k=len(newArr))
for i in range(0,len(newArr)):
  index = random_index[i]
  password += newArr[index]
print(password)