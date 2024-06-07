'''alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Print the entire alphabet


def encrypt(text, shift_key):
    cipher_text = " "
    for char in text:
        position = alphabet.index(char)
        new_position = (position + shift_key)%26
        cipher_text += alphabet[new_position]
    return cipher_text

def decrypt(cipher_text, shift_key):
    plain_text = " "
    for char in cipher_text:
        position = alphabet.index(char)
        new_position = (position - shift_key)%26
        
        plain_text += alphabet[new_position]
    return plain_text

text = input()
shift_key = int(input())
print(encrypt(text,shift_key), decrypt(text, shift_key))'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift_key):
    cipher_text = ""
    for char in text:
        if char in alphabet:  # Check if character is in the alphabet
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char  # Append the character as is (e.g., spaces, punctuation)
    return cipher_text

def decrypt(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:  # Check if character is in the alphabet
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char  # Append the character as is (e.g., spaces, punctuation)
    return plain_text

text = input("Enter the text to encrypt: ")
shift_key = int(input("Enter the shift key: "))
encrypted_text = encrypt(text, shift_key)
decrypted_text = decrypt(encrypted_text, shift_key)
print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")




