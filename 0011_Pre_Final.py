# imports
import random
import math


# intcheck code
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
            print()


# hl(pretty stuff around some outputs) code
def hl_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()
    return ""

# Main Routine starts here:

# keep_going code starts here
keep_going = ""
while keep_going == "":

    # high/low scale for secret
    lowest = intcheck("Low Number: ", 1, 100)
    highest = intcheck("High Number: ", lowest, 100000)

    # finding max amount of guesses
    num_range = highest - lowest + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1

    # ask for amount of rounds
    rounds = intcheck("How many rounds?", 1, 10)  #
    rounds_played = 0

    num_won = 0
    num_lost = 0

    while rounds_played < rounds:
        # output amount of rounds and guesses allowed
        start_round = hl_statement("### Round {} of {} ###".format(rounds_played + 1, rounds), "#")
        guesses_ya_get = hl_statement("=== You Get {} Guesses ===".format(max_guesses), "=")

        rounds_played += 1

        already_guessed = []
        guesses_left = max_guesses

        # generate secret
        secret = random.randint(lowest, highest)
        print(secret)

        guess = ""

        while guess != secret and guesses_left >= 1:
            # ask user for their Guess
            guess = intcheck("Guess: ", lowest, highest)  # replace later

            # see if Guess has already been Guessed(and give output)
            if guess in already_guessed:
                duplicate = hl_statement("!! You already guessed that # Please try again.    |    "
                                         "Guesses Left: {} !!".format(guesses_left), "!")
                continue

            guesses_left -= 1
            already_guessed.append(guess)

            if guesses_left >= 1:
                # comparing secret to Guess
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

        # first try and/or finished anyway, outputs
        if guess == secret:
            if guesses_left == max_guesses - 1:
                first_try = hl_statement("$$$ Amazing! You got it in one guess! $$$", "$")

                num_won += 1
            else:
                how_many_guesses = max_guesses - guesses_left
                well_done = hl_statement("*** Well done! You got it in {} guesses ***".format(how_many_guesses), "*")

                num_won += 1
        else:
            # losers output
            print("Sorry - you lose this round as you have run out of guesses")
            secret_num = hl_statement("!! The Secret Number was {} !!".format(secret), "!")

            num_lost += 1

        # final wins/losses tally/count
        print("Won: {} \t | \t Lost: {}".format(num_won, num_lost))

    print("You have gotten to the end of the game")

    # keep_going end
    keep_going = input("Press <enter> to play again or any other key to quit (With <enter> afterwards)")
    print()

# goodbye/farewell
print()
print("Thank You For Playing")
