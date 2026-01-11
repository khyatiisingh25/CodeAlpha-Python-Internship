import random

# words list given
words = ["apple", "banana", "python", "coding", "intern"]

# selecting random word
word = random.choice(words)

attempts = 6
guessed = ""   # storing guessed letters as string

print("Hangman Game")
print("Guess the word")
print("Total attempts:", attempts)

while attempts > 0:

    display = ""

    # checking each letter
    for i in range(len(word)):
        if word[i] in guessed:
            display = display + word[i]
        else:
            display = display + "_"

    print("\nWord:", display)

    # if word guessed
    if display == word:
        print("You guessed the word correctly")
        break

    letter = input("Enter a letter: ")
    letter = letter.lower()

    # adding guessed letter
    if letter not in guessed:
        guessed = guessed + letter
    else:
        print("Letter already entered")

    # wrong guess condition
    if letter not in word:
        attempts = attempts - 1
        print("Wrong guess")
        print("Remaining attempts:", attempts)

# game over condition
if attempts == 0:
    print("\nGame Over")
    print("Correct word was:",word)
    
    

