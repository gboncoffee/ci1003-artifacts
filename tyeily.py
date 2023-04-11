#!/usr/bin/env python3

import sys
import string


alphabet = list(string.ascii_letters)
alphabet = alphabet + [' ']
alphabet = alphabet + list(string.digits)
our_mod = len(alphabet)


def encrypt(msg, key):
    revert_flag = False
    for i, char in enumerate(msg):
        char = (char + key) % our_mod
        for j in range(0, i):
            if msg[j] % 2 == 0:
                revert_flag = not revert_flag
            if not revert_flag:
                char = (char + msg[j]) % our_mod
            else:
                char = (char + (our_mod - msg[j])) % our_mod
        msg[i] = char

    return msg


def decrypt(msg, key):
    revert_flag = True
    decrypted = list()
    for i, char in enumerate(msg):
        char = (char + (our_mod - key)) % our_mod
        for j in range(0, i):
            if msg[j] % 2 == 0:
                revert_flag = not revert_flag
            if not revert_flag:
                char = (char + msg[j]) % our_mod
            else:
                char = (char + (our_mod - msg[j])) % our_mod

        decrypted.append(char)

    return decrypted


try:
    key = int(sys.argv[2])
    what_to_do = sys.argv[1]
    callback = None
    if what_to_do == "encrypt" or what_to_do == "e":
        callback = encrypt
    else:
        callback = decrypt
    msg = sys.stdin.read()
    new_msg = list()
    for char in msg:
        try:
            i = alphabet.index(char)
            new_msg.append(i)
        except Exception:
            pass
    msg = callback(new_msg, key)
    for i, j in enumerate(msg):
        msg[i] = alphabet[j]
    print(''.join(msg))

except Exception:
    print("""
Usage: <prog> {e/d/encrypt/decrypt} <key>

Insert input via stdin, expect output via stdout.
    """)
    exit(1)
