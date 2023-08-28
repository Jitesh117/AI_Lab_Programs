import random

def choose_word():
    words = ["python", "programming", "hangman", "computer", "gaming", "language", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

            if attempts == 0:
                print("Sorry, you're out of attempts. The word was:", word)
                break
        else:
            word_display = display_word(word, guessed_letters)
            print(word_display)

            if "_" not in word_display:
                print("Congratulations! You've guessed the word:", word)
                break

hangman()
