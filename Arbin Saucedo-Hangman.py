import random
import string

"""
A general guide for Hangman
1. Make a word bank/ list of phrases, movies, etc. - 10 items
2. Pick a random item from the list 
3. Add a guess to the list of letters guessed
4. Reveal letters already guessed 
5. Create the win condition 
ULTIMATE HINT MY DUDE:output =['_','_','_','_','_','_' '_','_','_','_'] 
                      guesses_left 10
                      letters_guesses[???]
"""
guesses_left = 10

letters_guessed = []

word_bank = ["phone", "baseball", "aColdOne", "Meme", "gitGud", "boi", "clean", "list",
             "Shopping", "supercalifragilisticexpialidocious"]
random_word = word_bank[random.randint(0, len(word_bank) - 1)]

current_guess = ' '
win = False
while guesses_left > 0 and not win:
    output = []
    for letter in random_word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("_")

    print(" ".join(list(output)))

    if output == list(random_word):
        print("*You Win*")
        win = True
        continue
    current_guess = input("Type in a letter: ")
    letters_guessed.append(current_guess)
    print(letters_guessed)

    if current_guess not in random_word:
        guesses_left -= 1
        print(guesses_left)

