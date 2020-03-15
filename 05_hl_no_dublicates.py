#

#
#
#
#

#

SECRET = 7
GUESSES_ALLOWED = 5

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != SECRET and guesses_left >= 1:

        guess = int(input("Guess: "))  # replace later

        #
        if guess in already_guessed:
            print("You already guessed that number! Please try again. "
                  "You *still* have {} guesses left".format(guesses_left))
            continue

        guesses_left -= 1
        already_guessed.append(guess)

        if guesses_left >= 1:

            if guess < SECRET:
                print("Too low, try a lower number. Guesses left: {}". format(guesses_left))

            elif guess > SECRET:
                print("Too high, try a higher number. Guesses left: {}". format(guesses_left))
        else:
            if guess < SECRET:
                print("Too Low!")
            elif guess > SECRET:
                print("Too High!")

if guess == SECRET:
    if guesses_left == GUESSES_ALLOWED - 1:
        print("Amazing! You got it in one guess")
    else:
        print("Well done, you got it in {} guesses". format(len(already_guessed)))
    num_won += 1
else:
    print("Sorry - you lose this round as you have run out of guesses")
