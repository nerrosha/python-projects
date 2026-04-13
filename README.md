caesar-cipher-python

A simple Python program that encrypts an English text using a Caesar cipher, where each word is shifted by the length of that word (letters only).
Uppercase letters remain uppercase, lowercase letters remain lowercase, and non-letter characters are not changed.

How it works

For every word:

Count how many alphabetic characters it contains → this is the shift value.
Shift each letter forward in the alphabet by that amount (cyclic shift).
Preserve the original letter case.
Keep punctuation and other non-letter symbols unchanged.

Password Generator

A simple Python program that generates secure passwords based on user preferences.

Features

Generate multiple passwords
Custom password length
Optional inclusion of:
digits (0–9)
lowercase letters (a–z)
uppercase letters (A–Z)
symbols (!#$%&*+-=?@^_)
Option to exclude ambiguous characters (il1Lo0O)
How it works

The user selects password settings.
The program builds a pool of allowed characters.
Passwords are generated randomly using the selected character set.
