import random

secret = random.randint(1, 100)
guess, tries = 0, 0

#for i in range(6):
while tries < 6:
    print("pls guess the number:")
    guess = int(input())
    if guess == secret:
        print("You are a lucky man! You guessed it! The number is %d" % secret)
        print("You guessed %d times!" % (tries+1)) 
        break
    elif guess > secret:
        print("You guessed is too larger!")
    elif guess < secret:
        print ("you guessed is too small!")
    tries += 1
else:
    print("You wasted too many times!")
    print("The number is %d" % secret)
