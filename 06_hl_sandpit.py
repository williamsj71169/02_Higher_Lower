

def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()
    return ""

fish = 6
cat = 1

decoration = "^"

feedback = "^^ Too low, try a higher number.    |    Guesses Left: {} ^^".format(cat)
tooo_low = hl_statement(feedback, decoration)

too_low = hl_statement("^^ Too low, try a higher number.    |    "
                       "Guesses Left: 3 ^^".format(cat), "^")

print()
too_high = hl_statement("vv Too high, try a lower number.    |    "
                       "Guesses Left: {} vv".format(cat), "v")


end_low = hl_statement("^^ Too Low!,  ^^", "^")

end_high = hl_statement("vv Too Low!,  vv", "v")



print()
duplicate = hl_statement("!! You already guessed that # Please try again.    |    "
                       "Guesses Left: {} !!".format(cat), "!")
print()
well_done = hl_statement("*** Well done! You got it in {} guesses ***".format(cat), "*")

first_try = hl_statement("$$$ Amazing! You got it in one guess! $$$", "$")



print()
start_round = hl_statement("### Round {} of {} ###".format(cat, fish), "#")
