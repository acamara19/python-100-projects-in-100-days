"""
caesar-cipher-1-start
"""
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceasar_cipher(cipher_text, shift_amount, cipher_direction):
    message = ""
    if cipher_direction == "decrypt":
        shift_amount *= -1
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            message += alphabet[new_position]
        else:
            message += char
    print(f"The {cipher_direction}ed text is: {message}")


end_game = False
while not end_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: "))
    shift = shift % 26

    ceasar_cipher(cipher_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if restart == "yes":
        end_game = False
    elif restart == "no":
        end_game = True
        print("Goodbye")
