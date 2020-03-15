#

import math

for item in range(0, 4):



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


    low = intcheck("Low: ", 1, 100)
    high = intcheck("High: ", 1, 100000)

    range = high - low + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))

    print()
