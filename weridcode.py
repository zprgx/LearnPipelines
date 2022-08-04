#!/usr/bin/python3
from sys import argv

try:
    msg = argv[1]
    print(f"You said: {msg[::-1]}")
except IndexError:
    print("LMAO Werido")
