import random

random.randint(1, 6)

money = 15

rounds = 0

most = money

win = 0
lose = 0

print("Gambler Guy: Hey there I see you in a bit of a pickle")
print("Gambler Guy: That's why your drinking away aren't you")
print("Gambler Guy: Not much of a talker huh")
print("Gambler Guy: Well I tell you what how bout you gamble a bit")
print("Gambler Guy: You might get some money out of it you never know")
print("Gambler Guy: So we got a deal")
print("You Maybe: Alright")
print("Gambler Guy: Lucky 7's it is then time to start")

while money > 0:
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)

    if Dice1 + Dice2 == 7:
        print("Gambler Guy: wow you won, lucky man")
        money += 4
        print("Money = %s" % money)
        win += 1
        if money > most:
            most = money

    else:
        print("Gambler Guy: tough luck")
        money -= 1
        print("Money = %s" % money)
        lose += 1

    rounds += 1

    if money == 0:
        print("Gambler Guy: Looks like you ran out of money to bad... now leave")


print("Rounds = %s" % rounds)
print("Gambler Guy: you won %s time(s)" % win)
print("Gambler Guy: you lost %s time(s)" % lose)
print("Gambler Guy: well the most you had was %s" % most)


