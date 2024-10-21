alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
logo = """                              
           88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""" """" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88     
              
"""

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
t = input("Type your message:\n").lower()
s = int(input("How many shifts do you want?\n"))
s = s % 26

cipher(text=t, shift=s, direction=direction)

# def encrypt(text, shift):
#   cipher_text = ""
#   for letter in text:
#     # finding the position (index) of the letter in the alphabet list
#     position = alphabet.index(letter)
#     # calculating new position by adding shift
#     new_position = position + shift
#     # grab the new letter from the alphabet based on the new position
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The encoded text is {cipher_text}")

# def decrypt(text, shift):
#   decipher_text = ""
#   for letter in text:
#     position = alphabet.index(letter)
#     # same as encode but new_position is subtraction of current position and shifts
#     new_position = position - shift
#     new_letter = alphabet[new_position]
#     decipher_text += new_letter
#   print(f"The encoded text is {decipher_text}")


def cipher(text, shift, direction):
  cipher = ""
  if direction == "decode":
    shift *= -1
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift
      cipher += alphabet[new_position]
    else:
      cipher += char
  print(f"Here's the {direction}d result: {cipher}")




replay = input("Press Y to start over \n").lower()
if replay == "y":
 

# if direction == ("encode"):
#   encrypt(text=t, shift=s)
# elif direction == ("decode"):
#   decrypt(text=t, shift=s)
