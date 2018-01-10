import random

random.randint(1, 6)

money = 15

print("Bartender: Hey there I see you in a bit of a pickle")
print("Bartender: Thats why your drinking away aren't you")
print("Bartender: Not much of a talker huh")
print("Bartender: Well I tell you what how bout you gamble a bit")
print("Bartender: You might get some money out of it you never know")
print("Bartender: So we got a deal")
print("You Maybe: Alright")
print("Bartender: Lucky 7's it is then time to start")

while money > 0:
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)

    if Dice1 + Dice2 == 7:
        print("Bartender: wow you won, lucky man")
        money += 4

    else:
        print("Bartender: tough luck")
        money -= 1

    if money == 0:
        print("Bartender: Looks like you ran out of money to bad... now leave")


rounds = 0

if print("Bartender: tough luck"):
    rounds += 1

print("Rounds = %s" % rounds)
