import random
import string

from words import wordBank


def get_valid_word(dictionary):
    word = random.choice(dictionary)
    while '-' in word or ' ' in word:
        word = random.choice(dictionary)

    return word.upper()


def hangman():
    word = get_valid_word(wordBank)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10

    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f"You have {lives} lives left. You have used these letters: ", " ".join(used_letters))

        # what the current word is (W - O R D)
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", ' '.join(word_list))

        # getting user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:  # check if user_letter is in alphabet and not in used_letters
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print("Letter is not in word.")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again")

        else:
            print("Invalid character. Please try again.")

        print()

    if lives == 0:
        print("Sorry, you died ! The word was ", word)
    else:
        print("Yay, you guessed the word ", word, "!!")


hangman()
