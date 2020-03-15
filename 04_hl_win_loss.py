#

#
#
#
#
#

SECRET = 7
GUESSES_ALLOWED = 4

#
guesses_left = GUESSES_ALLOWED
num_won = 0
num_lost = 0
guess = ""

# Start Game
while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))
    guesses_left -= 1

    # if have guess left
    if guesses_left >= 1:
        if guess < SECRET:
            print("Too Low, try a higher number")

        if guess > SECRET:
            print("Too High, try a lower number")

    else:
        if guess < SECRET:
            print("Too Low")

        if guess > SECRET:
            print("Too High")

if guess == SECRET:
    # if got first time
    if guesses_left == GUESSES_ALLOWED:
        print("Amazing! You got it in one guess")
        num_won += 1

    # if had more then  one guess....
    else:
        print("Well Done! You got it in {} tries".format(guesses_left))
        num_won += 1

# uses ran out(and loses)
else:
    print("Sorry - you lose this round as you have run out of guesses")
    num_lost += 1
