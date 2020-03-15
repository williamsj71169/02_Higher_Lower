#

SECRET = 7

guess = ""

while guess != SECRET:

        guess = int(input("Guess: "))  # replace later

        if guess < SECRET:
            print("Too low, try a lower number")
        elif guess > SECRET:
            print ("Too high, try a higher number")
        else:
            print ("Well done! You guessed the SECRET number")
