
health = 300


class Item(object):
    def __init__(self, name):
        self.name = name

    def pickup(self):
        print("You have picked up an item")


class Health(Item):
    def __init__(self, name):
        super(Health, self).__init__(name)

    def heal(self):
        print("You have healed yourself with healing item")


class Fairybottle(Health):
    def __init__(self, name):
        super(Fairybottle, self).__init__(name)

    def bottle_healing(self, target):
        if target.health < 100:
            target.health += 100


class Heartcontainer(Health):
    def __init__(self, name):
        super(Heartcontainer, self).__init__(name)

    def container_heal(self, target):
        if target.health < 300:
            target.health += 100


class Food(Health):
    def __init__(self, name):
        super(Food, self).__init__(name)

    def foodheal(self, target):
        if target.health < 300:
            target.health += 10


class Fightingitem(Item):
    def __init__(self, name):
        super(Fightingitem, self).__init__(name)


class SuperStrong(Fighting_item):
    def __init__(self, name, damage):
        super(SuperStrong, self).__init__(name)


class xbomb(SuperStrong):
    def __init__(self, name):
        super(xbomb, self).__init__(name, 65)

    def xboom(self):
        print("X-Bomb has exploded and damaged you damaged enemy")


class Masterball(SuperStrong):
    def __init__(self, name):
        super(Masterball, self).__init__(name, 80)

    def legendarypoke(self):
        print("You have spawned in a legendary pokemon that hurts your "
              "enemy badly")


class HomeRunBat(SuperStrong):
    def __init__(self, name):
        super(HomeRunBat, self).__init__(name, 100)

    def HOMERUN(self):
        print("YOU HUT A HOME RUN AND DID HUGE DAMAGE TO YOUR ENEMY")


class bob_omb(SuperStrong):
    def __init__(self, name):
        super(bob_omb, self).__init__(name, 80)

    def BIGBOOM(self):
        print("You threw a Bob-Omb and did a lat a damege")


class SmashBall(SuperStrong):
    def __init__(self, name):
        super(SmashBall, self).__init__(name, 150)

    def SMASH(self):
        print("You have Unleashed your final move on your opponent "
              "and caused MASSIVE Damage")


class MeleeItems(Fighting_item):
    def __init__(self, name, damage):
        super(MeleeItems, self).__init__(name)


class Fan(MeleeItems):
    def __init__(self, name):
        super(Fan, self).__init__(name, 15)

    def wak(self):
        print("You have waked the Hecc out of your enemy")


class Fire_flower(MeleeItems):
    def __init__(self, name):
        super(Fire_flower, self).__init__(name, 30)

    def burn(self):
        print("You burned your enemy it did decent damage")


class Beam_sword(MeleeItems):
    def __init__(self, name):
        super(Beam_sword, self).__init__(name, 40)

    def beam_slash(self):
        print("You slashed your enemy with a beam it did good damage")


class RangedItems(Fighting_item):
    def __init__(self, name, damage):
        super(RangedItems, self).__init__(name)


class green_shell(RangedItems):
    def __init__(self, name):
        super(green_shell, self).__init__(name, 20)

    def shelled(self):
        print("You hit your enemy with a green shell nice shot")


class ray_gun(RangedItems):
    def __init__(self, name):
        super(ray_gun, self).__init__(name, 55)

    def pew_pew(self):
        print("You keep shooting a your enemy and it did good damage also pew pew")


class Freezie(RangedItems):
    def __init__(self, name):
        super(Freezie, self).__init__(name, 10)

    def frozen(self):
        print("You have froze your enemey attack him with what you got")


class Pokeball(RangedItems):
    def __init__(self, name):
        super(Pokeball, self).__init__(name, 75)

    def pokemon(self):
        print("You threw the pokeball and a pokemon came out and attacked your enemey")


class MrSaturn(RangedItems):
    def __init__(self, name):
        super(MrSaturn, self).__init__(name, 5)

    def stun(self):
        print("You threw Mr.Saturn and it hit your enemy if he had his shield on he was stunned"
              "if not it didn't do much damage")


class Keys(Item):
    def __init__(self, name):
        super(Keys, self).__init__(name)

    def open(self):
        print("You have got the four keys and opened the final door")


class DL64key(Keys):
    def __init__(self, name):
        super(DL64key, self).__init__(name)

    def closeDL64(self):
        print("You have picked up the key that gets you closer to the end")


class KJ64key(Keys):
    def __init__(self, name):
        super(KJ64key, self).__init__(name)

    def closeKJ64(self):
        print("You are getting closer to the end")


class GDI(Keys):
    def __init__(self, name):
        super(GDI, self).__init__(name)

    def closeGDI(self):
        print("There are other keys but if you find them then the end is close")
