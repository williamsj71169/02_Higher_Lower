#

#
#
#


SECRET = 7
GUESSES_ALLOWED = 4
rounds = 3

num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = GUESSES_ALLOWED

    while guess != SECRET and guesses_left >= 1:

        guess = int(input("Guess: "))  # replace later
        guesses_left -= 1

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
            print("Well done, you got it in {} guesses". format(GUESSES_ALLOWED - guess))
        num_won += 1
    else:
        print("Sorry - you lose this round as you have run out of guesses")

    print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1
