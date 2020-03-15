import random
# import math


LOW = 1
HIGH = 100


def intcheck(question, low, high):
    valid = False
    error = "Please enter an integer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)


def hl_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()
    return ""
#

rounds = intcheck("How many rounds?", 1, 10)  #
rounds_played = 0

keep_going = ""
while keep_going == "":

    num_won = 0
    num_lost = 0

    while rounds_played < rounds:
        start_round = hl_statement("### Round {} of {} ###".format(rounds_played + 1, rounds), "#")

        rounds_played += 1

        GUESSES_ALLOWED = intcheck("How many guesses would you like? (1-25)", 1, 25)

        already_guessed = []
        guesses_left = GUESSES_ALLOWED

        secret = random.randint(LOW, HIGH)
        print(secret)

        guess = ""

        while guess != secret and guesses_left >= 1:

            guess = intcheck("Guess: ", 1, 100)  # replace later

            #
            if guess in already_guessed:
                duplicate = hl_statement("!! You already guessed that # Please try again.    |    "
                                         "Guesses Left: {} !!".format(guesses_left), "!")
                continue

            guesses_left -= 1
            already_guessed.append(guess)

            if guesses_left >= 1:

                if guess < secret:
                    too_low = hl_statement("^^ Too low, try a higher number.    |    "
                                           "Guesses Left: {} ^^".format(guesses_left), "^")

                elif guess > secret:
                    too_high = hl_statement("vv Too high, try a lower number.    |    "
                                            "Guesses Left: {} vv".format(guesses_left), "v")
            else:
                if guess < secret:
                    end_low = hl_statement("^^ Too Low!,  ^^", "^")
                elif guess > secret:
                    end_high = hl_statement("vv Too High!,  vv", "v")

        if guess == secret:
            if guesses_left == GUESSES_ALLOWED - 1:
                first_try = hl_statement("$$$ Amazing! You got it in one guess! $$$", "$")

                num_won += 1
            else:
                how_many_guesses = GUESSES_ALLOWED - guesses_left
                well_done = hl_statement("*** Well done! You got it in {} guesses ***".format(how_many_guesses), "*")

                num_won += 1
        else:
            print("Sorry - you lose this round as you have run out of guesses")
            print("The Secret Number was {}".format(secret))
            secret_num = hl_statement("!! The Secret Number was {} !!".format(secret), "!")

            num_lost += 1

        print("Won: {} \t | \t Lost: {}".format(num_won, num_lost))

    print("You have gotten to the end of the game")

    keep_going = input("Again?")
    if keep_going != "":
        print("Thank You For Playing!")
