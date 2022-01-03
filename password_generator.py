import random

# Prompt the User to enter a weak password 

print("Hi! This program allows you to enter a weak password (Preferably all lowercase letters), and then it generates a stronger and more secure password for you!")

weak_password = input('Start by inserting a weak password: ')

strong_password = ""

# Generate a strong password

for old_character in weak_password:
  if old_character == "a":
    options = ["E", "2", "4", "R", "7", "a"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character

  elif old_character == "b":
    options = ["1", "2", "b", "J", "7", "b"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character
  
  elif old_character == "c":
    options = ["7", "2", "!", "Z", "3", "c"]
    new_character = random.choice(options)
  
  elif old_character == "d":
    options = ["6", "3", "O", "T", "7", "d"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character

  elif old_character == "e":
    options = ["4", "2", "?", "Y", "9", "e"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character

  elif old_character == "f":
    options = ["L", "2", "7", "X", "#", "f"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character


  elif old_character == "g":
    options = ["#", "2", ">", "N", "7", "g"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character


  elif old_character == "h":
    options = ["h", "2", "4", "M", "9", "h"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character

  elif old_character == "i":
    options = ["3", "2", "<", "S", "6", "i"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character


  elif old_character == "j":
    options = ["j", "5", "@", "T", "7", "j"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character


  elif old_character == "k":
    options = ["1", "6", "R", "I", "7", "k"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character
 
  elif old_character == "l":
    options = ["i", "2", "!", "H", "7", "l"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character


  elif old_character == "m":
    options = ["3", "2", "7", "P", "11", "m"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character


  elif old_character == "n":
    options = ["1", "4", "!", "3", "M", "n"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character

  elif old_character == "o":
    options = ["4", "9", "%", "B", "2", "o"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character
 

  elif old_character == "p":
    options = ["1", "2", "p", "A", "7", "p"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character

  elif old_character == "q":
    options = ["q", "2", "!", "Q", "7", "q"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character


  elif old_character == "r":
    options = ["8", "2", "$", "W", "7", "r"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character


  elif old_character == "s":
    options = ["s", "2", "@", "D", "7", "s"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character


  elif old_character == "t":
    options = ["1", "0", "#", "H", "9", "t"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character

  elif old_character == "u":
    options = ["u", "2", "~", "O", "3", "u"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character

  elif old_character == "v":
    options = ["D", "0", "?", "H", "7", "v"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character


  elif old_character == "w":
    options = ["w", "K", "!", "H", "7", "w"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character

  elif old_character == "x":
    options = ["9", "0", "&", "J", "7", "x"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character

  elif old_character == "y":
    options = ["y", "5", "!", "G", "3", "y"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character


  elif old_character == "z":
    options = ["6", "2", "*", "L", "7", "z"]
    new_character = random.choice(options)
    strong_password = strong_password + new_character

  else:
    strong_password  = strong_password + old_character


# Print the new password 
print ("Here is your new strong password: " + (strong_password)) 

if len(strong_password) < 8:
  print("Warning : Your password is going to be less than 8 characters. \n For more security, it is recommended to have a password longer than 8 characters.")