import random
# 1) Generate random number
# 2) Take on input (number) from the user/ Ask The user for an input
# 3) Compare input to generated number
# 4) Add "Higher" and "Lower" statements
# 5) Add 5 guesses

randomNum = random.randint(1, 50)

guess = int(input(" "))

if guess == randomNum:
    print(" GUNGUS ")

elif guess >= randomNum:
    print("Your Guess is higher than Number")

elif guess <= randomNum:
    print("Your Guess is lower than Number")



