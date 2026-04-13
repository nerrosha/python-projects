# Python Projects

This repository contains two small Python projects: a Caesar cipher program and a password generator. They were made for practice and to improve basic programming skills.

---

## Caesar Cipher (Python)

A simple program that encrypts English text using a Caesar cipher. Each word is shifted by the number of letters in that word.

### How it works
- Each word is processed separately  
- The shift value is the number of letters in the word  
- Letters are shifted forward in the alphabet (cyclic)  
- Uppercase stays uppercase, lowercase stays lowercase  
- Non-letter characters (spaces, punctuation, etc.) are not changed  

---

## Password Generator (Python)

A simple program that generates random passwords based on user preferences.

### Features
- Generate one or multiple passwords  
- Set custom password length  
- Choose character types:
  - lowercase letters
  - uppercase letters
  - numbers
  - symbols  
- Option to exclude similar/ambiguous characters (like il1Lo0O)

### How it works
- User selects password options  
- Program builds a set of allowed characters  
- Passwords are generated randomly from that set  
