import random

secret = random.randint(1, 100)
guess, tries = 0, 0

for i in range(6):
    print("pls guess the number:")
    guess = int(input())
    tries += 1
    if guess == secret:
        print("You are a lucky man! You guessed it!")
        break
    elif guess > secret:
        print("You guessed is too larger!")
    elif guess < secret:
        print ("you guessed is too small!")

if tries < 6:
    print("You guessed %d times!" % tries)
else:
    print("You wasted too many times!")
