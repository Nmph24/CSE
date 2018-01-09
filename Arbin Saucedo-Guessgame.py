import random
# 1) Generate random number
# 2) Take on input (number) from the user/ Ask The user for an input
# 3) Compare input to generated number
# 4) Add "Higher" and "Lower" statements
# 5) Add 5 guesses

randomNum = random.randint(1, 50)

name = input("Name: ")

print("Hello %s today you will guess a random number" % name)

print(",But you will only have 5 trys to guess the number.")

print("So Good Luck %s" % name)

print("*Start*")

guesses = 5
guess = -1

while guesses > 0 and guess != (str(randomNum)):
    guess = int(input(" "))

    if guess == randomNum:
        print(" boom done happy good time goodnight ")
        print("Number is %d" % randomNum)
        guesses = -1

    elif guess >= randomNum:
        print("Sorry, Your Guess is higher than Number try again.")
        guesses -= 1

    elif guess <= randomNum:
        print("Nope, Your Guess is lower than Number give another guess")
        guesses -= 1

if guesses == 0:
    print("You ran out of guess ")
    print("*GAME OVER*")
    print("Number was %d" % randomNum)

if guesses == -1:
    print(" YOU DID IT GREAT JOB ")
    print("*YOU WIN*")
