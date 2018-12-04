# Dakota Bourne (db2nb) Nick Manalac (ntm4kd) Justin Lakier (Jel5hv)
"""

"""


def encrypt(plain_text, key):
    cipher_text = '' # accumulator pattern: start with no encrypted test
    for i in range(0, len(plain_text), 1): # look one chunk at a time
        chunk = plain_text[i:i+1]          # all chunks the same size
        cipher_text += encrypt_chunk(chunk, key)    # most work is in another function
    return cipher_text


def encrypt_chunk(chunk, key):
    if chunk == " ":
        return " "
    else:
        return chr(ord(chunk) + key)

print(encrypt("black people", 3))
print(list("black people"))