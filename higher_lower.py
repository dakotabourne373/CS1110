# Dakota Bourne db2nb
"""
The purpose of this program is to take user inputs and depending on the input for the answer, either generate a new
number or use the number given by the user to play a guessing game.
"""
import random
answer = int(input("What should the answer be? "))
guesses = int(input("How many guesses? "))
if answer == -1:
    answer = random.randrange(1, 100)
while guesses != 0:
    guesses -= 1
    guess = float(input("guess a number: "))
    if guess < answer:
        print("The number is higher than that.")
    elif guess > answer:
        print("The number is lower than that.")
    else:
        print("You win!")
        guesses = 0
    if guesses == 0 and guess != answer:
        print("You lose; the number was " + str(answer))
