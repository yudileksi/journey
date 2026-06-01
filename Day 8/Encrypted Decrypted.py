import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"Chars   : {chars}")
# print(f"Keys    : {key}")

# ENCRYPT
plain_text = input("Enter massage to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original massage    :{plain_text}")
print(f"Encrypted massage   :{cipher_text}")

# DECRYPT
cipher_text = input("Enter massage to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Original massage    :{cipher_text}")
print(f"Decrypted massage   :{plain_text}")

