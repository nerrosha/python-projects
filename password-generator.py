import random

# character sets
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!#$%&*+-=?@^_'

available_chars = ''

# user input
num_passwords = int(input('Enter number of passwords to generate: '))
password_length = int(input('Enter password length: '))

include_digits = input('Include digits? (y/n) ').strip().lower()
include_lowercase = input('Include lowercase letters? (y/n) ').strip().lower()
include_uppercase = input('Include uppercase letters? (y/n) ').strip().lower()
include_symbols = input('Include symbols (!#$%&*+-=?@^_)? (y/n) ').strip().lower()
exclude_ambiguous = input('Exclude ambiguous characters (il1Lo0O)? (y/n) ').strip().lower()

# configure character pool
if include_digits == 'y':
    available_chars += digits

if include_lowercase == 'y':
    available_chars += lowercase_letters

if include_uppercase == 'y':
    available_chars += uppercase_letters

if include_symbols == 'y':
    available_chars += symbols

if exclude_ambiguous == 'y':
    for ch in 'il1Lo0O':
        available_chars = available_chars.replace(ch, '')

# password generation function
def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

# generate passwords
for _ in range(num_passwords):
    print(generate_password(password_length, available_chars))