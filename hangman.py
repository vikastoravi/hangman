import random

# List of words to choose from
word_list = ["python", "hangman", "developer", "keyboard", "function", "variable"]

# Choose a random word from the list
secret_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

# Display the word with underscores for unguessed letters
def display_word():
    displayed = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed.strip()

print("🎮 Welcome to Hangman!")
print(f"You have {max_incorrect_guesses} incorrect guesses. Good luck!")

# Main game loop
while True:
    print("\nWord:", display_word())
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        print(f"❌ Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} tries left.")

    # Check if the word is completely guessed
    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Check if the player has run out of guesses
    if incorrect_guesses >= max_incorrect_guesses:
        print("\n💀 Game Over! The word was:", secret_word)
        break
