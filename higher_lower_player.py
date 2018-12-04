# Dakota Bourne db2nb
"""
This program is designed to have a user play a random number guessing game, where the computer prompts the user for
input on whether or not it is getting closer of not, essentially until it guess the right number.
"""
print("Think of a number between 1 and 100 and I'll guess it.")
guesses = int(input("How many guesses do I get? "))
low = 0
high = 100
while guesses != 0:
    guesses -= 1
    guess = int((low + high) // 2)
    answer = str(input("Is the number higher, lower, or the same as " + str(guess) + " "))
    if answer == "higher":
        low = guess
    elif answer == "lower":
        high = guess
    elif answer == "same":
        print("I won!")
        break
    if low == (guess - 1) or high == (guess + 1):
        print("Wait; how can it both be higher than " + str(low), "and lower than " + str(high) + "?")
        break
    if guesses == 0 or answer == "higher" and answer == "lower":
        float(high)
        fin_answer = float(input("I lost; what was the answer? "))
        if fin_answer >= high:
            print("That can't be; you said it was lower than " + str(high) + "!")
        elif fin_answer <= high:
            print("That can't be; you said it was higher than " + str(low) + "!")
        else:
            print("Well played!")
