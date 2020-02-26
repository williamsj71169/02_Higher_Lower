#


import random

LOW = 1
HIGH = 1

for item in range(1, 20):
    secret = random.randint(LOW, HIGH)
    print(secret, end="\t")
