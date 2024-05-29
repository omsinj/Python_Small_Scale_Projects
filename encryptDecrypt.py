import string
import random
alphabet = string.ascii_letters

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message: \n"). lower()

shift = int(input("Type the shift number:\n")


def encrypt(plain_text, shift_amount):
    alphabet = string.ascii_letters
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"the encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    alphabet = string.ascii_letters
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"the decoded text is {plain_text}")

def ceaser(start_text, shift_amount, cipher_direction):
    alphabet = string.ascii_letters
    end_text = " "
    
    if cipher_direction == 'decode':
            shift_amount *= -1

    for letter in start_text:
        position = alphabet.index(letter)
        
        new_position = position + shift_amount
        end_text += alphabet[new_position]

    print(f"the answer is {end_text}")
