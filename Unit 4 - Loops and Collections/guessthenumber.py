# Guess the number
import random

guess = -1
number = random.randint(0,101)

while guess != number:

    try:
        guess = int(input("Whats your guess?\n>"))
        if guess > number:
            print("Too large, try again...")
    
        elif guess < number:
            print("Too small, try again...")
    
        else:
            print("Bingo! The correct number was " + str(number))

    except:
        print("Hmm... That's not right...")

   
print("Nice job")