
import random

# List of 5 predefined words
words = ["python", "apple", "tiger", "computer", "flower"]

# Select a random word
word = random.choice(words)

guessed_word = ["_"] * len(word)
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")
print("Guess the hidden word letter by letter.")

while wrong_guesses < max_attempts and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses:", wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        print("Wrong guess!")
        wrong_guesses += 1

# Check the result
if "_" not in guessed_word:
    print("\nCongratulations! You Won!")
    print("The word is:", word)

else:
    print("\nGame Over!")
    print("The correct word was:", word)