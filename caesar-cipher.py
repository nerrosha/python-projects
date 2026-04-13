text = input()
encrypted_words = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for current_word in text.split():
    # calculate shift value for the current word (number of letters)
    shift_count = 0
    for letter in current_word:
        if letter.isalpha():
            shift_count += 1

    # build encrypted word
    encrypted_word = ''
    for letter in current_word:
        # check if the character is a letter
        if letter.isalpha():
            # find position of the letter in the alphabet
            position = alphabet.index(letter.lower())

            # calculate new position with cyclic shift
            shifted_position = (position + shift_count) % 26

            # get new letter
            shifted_letter = alphabet[shifted_position]

            # preserve original case
            if letter.isupper():
                shifted_letter = shifted_letter.upper()

            encrypted_word += shifted_letter
        else:
            # keep non-letter characters unchanged
            encrypted_word += letter

    encrypted_words.append(encrypted_word)

print(*encrypted_words, sep=' ')