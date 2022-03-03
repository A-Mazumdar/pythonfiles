import random

UpperLimit = 9

x = random.randint(1, UpperLimit)

while(True):
    try:
        guess = int(input(f"Enter an integer from 1 to {UpperLimit}:  "))

    except ValueError:

        print("")
        print("Enter an Integer only!")
        print("")
        continue

    if guess is x:
        print("you guessed it!")
        break

    elif guess < x:
        print("guess is low")

    elif guess > x:
        print("guess is high")
