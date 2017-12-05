import random
# 1) Generate random number
# 2) Take on input (number) from the user/ Ask The user for an input
# 3) Compare input to generated number
# 4) Add "Higher" and "Lower" statements
# 5) Add 5 guesses

# print(random.randint(0, 50))


# def random_number(number):
#    print(random.randint(0, 50))


#def guess(number):
    # if number >= 60:
    #     return "Number Too High"
    # elif number >= 60:
    #     return "Number Too High"
    # elif number == 60:
    #     return "Correct"
    # elif number >= 60:
    #     return "Number too Low"
    # else:
    #     return "Number too Low"


# guess = input(" ")
# print("Is The Number %s?" % guess)

random = random.randint(1, 50)

def guess(number_guess):
    if number_guess >= random:
        return "Number is too High"
    elif number_guess == random:
        return "Number Is Correct"
    elif number_guess <= random:
        return "Number is too Low"


print(guess(10))
# guessNum = input (" ")
# print("Is number %s" % guessNum)


