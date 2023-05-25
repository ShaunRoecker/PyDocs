import math
from alphabet import alphabet
from art import logo
import os, platform


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def paint_calc(height: int, width: int, cover: int)-> None:
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint")

# paint_calc(2, 4, 5)


# Prime numbers can only be divided by itself and one
def prime_checker(num: int)-> bool:
    is_prime = True
    for n in range(2, num):
        if num % n == 0:
            is_prime = False
    if is_prime:
        return True
    return False

# print(prime_checker(5))

def encrypt(text: str, shift: int):
        cipher_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(cipher_text)


def decrypt(cypher_text: str, shift_amount: int)-> None:
    decoded_text = ""
    for letter in cypher_text:
        postition = alphabet.index(letter)
        new_position = postition - shift_amount
        decoded_text += alphabet[new_position]
    print(decoded_text)



def cryptokoder()-> None:
    print(logo)

    def caesar(text: str, shift: int, direction: str)-> None:
        new_text = ""
        if direction == "decode":
                shift *= -1
        for char in text:
            if char in alphabet:     
                position = alphabet.index(char)
                new_position = position + shift
                new_text += alphabet[new_position]
            else:
                new_text += char
        print(new_text)

    should_continue = True
    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        caesar(text, shift, direction)
        result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if result == "no":
            should_continue = False
            print("Goodbye")
       

cryptokoder()


