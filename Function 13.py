import random


def guess(n, true, count):
    if n == true:
        print("Good job, KBTU! You guessed my number in", count, "guesses!")
        return
    elif n < true:
        n = int(input("Your guess is too low.\nTake a guess.\n"))
        guess(n, true, count + 1)
    elif n > true:
        n = int(input("Your guess is too high.\nTake a guess.\n"))
        guess(n, true, count + 1)


name = input("Hello! What is your name?\n")
n = int(input("Well, " + name + ", I am thinking of a number between 1 and 20.\nTake a guess.\n"))
true = random.randint(1, 20)
count = 1
guess(n, true, count)
