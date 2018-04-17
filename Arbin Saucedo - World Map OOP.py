class Room(object):
    def __init__(self, name, description, enemey, s, n, e, w):
        self.name = name
        self.desc = description
        self.fighters = enemey
        self.north = n
        self.south = s
        self.east = e
        self.west = w

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Fighter(object):
    def __init__(self, name, description, health, dialogue, moves,
                 move_description):
        self.name = name
        self.description = description
        self.hel = health



health = 300


class Item(object):
    def __init__(self, name):
        self.name = name

    def pick_up(self):
        print("You have picked up an item")


class Health(Item):
    def __init__(self, name):
        super(Health, self).__init__(name)

    def heal(self):
        print("You have healed yourself with healing item")


class Fairy_bottle(Health):
    def __init__(self, name):
        super(Fairy_bottle, self).__init__(name)

    def bottle_healing(self, target):
        if target.health < 100:
            target.health += 100


class Heart_container(Health):
    def __init__(self, name):
        super(Heart_container, self).__init__(name)

    def container_heal(self, target):
        if target.health < 300:
            target.health += 100


class Food(Health):
    def __init__(self, name):
        super(Food, self).__init__(name)

    def food_heal(self, target):
        if target.health < 300:
            target.health += 10


class Fighting_item(Item):
    def __init__(self, name):
        super(Fighting_item, self).__init__(name)


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


Mario = Fighter("Mario", "Mario is an all around fighter that has a good move set that can be used in alot of"
                "different ways", 300, "Lets a Go", "Cape, Super Jump Punch, Mario Tornado, Fireball", "Cape:"
                 "This move turns around your opponent from the way they are facing, Super Jump Punch: This allows"
                 "you to get a high jump while still attacking your opponent and it is a good recovery, Mario Tornado:"
                 "Mario will spin around like a tornado while attacking the opponent, Fireball: This is a small ball"
                 "of fire Mario can shoot")


# Initialize Rooms(Have Not Started the control)
journey_hallway = Room("Journey Hall", "You have arrived at a hallway that will lead you into "
                       "many battles in this world to show your the best fighter out there", None, 'Temple',
                       None, 'Tangerine_Castle', None)

Temple = Room("Temple", "The Lowrule Temple where your first fight begins"
                       "with Princess Zelda so good luck on this map of fights because there are"
                       "so many more fights to come", "Zelda", "Cold_Place", None, "Fountain_Of_Sleep", None)

Tangerine_Castle = Room("Tangerine Castle", "The Castle of the Olive Kingdom and your first fight "
                        "with Princess Tangerine", "Princess Peach", "Fountain_Of_Sleep", None, "Olive_Kingdom",
                        None)

Fountain_Of_Sleep = Room("Fountain Of Sleep", "Now you are extra sleepy but you can fight still "
                         "so be happy for that but you now you up against "
                         "a harder characters because you have chosen the short "
                         "but harder path to the end so you are up against "
                         "Jigglypuff played by HBox", "Jigglypuff played by HBox", None, None, "Blue_Blues", None)

Olive_Kingdom = Room("Olive Kingdom", "This is the Olive Kingdom the home of Mario,"
                     "Dr.Mario, and Luigi and here you will be "
                     "Fighting Mario so START", "Mario", None, None, "Olive_Kingdom_2", None)

Cold_Place = Room("Cold Place", "The Coldest place out of this whole world"
                  "which is also mount everest and here you "
                  "are fighting 2 people that are one fighther"
                  "Ice Climbers", "Ice CLimbers", "Loud_City", None, None, None)

Blue_Blues = Room("Blue Blues", "Now it gets harder from here in blue blues so now "
                  "your up against Sheik played by Plup ,so good "
                  "luck cause its a top tier", "Shiek played by Plup", None, None, "Gren_Dino_Island64", None)

Olive_Kingdom_2 = Room("Olive Kingdom 2", "This is the other side of the Olive Kingdom where you "
                       "are slowly entering the jungle to fight someone else "
                       "but for now you up against Luigi", "Luigi", None, None, "Jungle_Japes", None)

Loud_City = Room("Loud City", "Well your in the city know and well this place looks like it has more of "
                 "an advance in car technology and there is still fighters here so don't"
                 "let the cars distract you anyways now your up against Pichu a small mice but "
                 "dont let that fool you he still packs a good punch", "Pichu", "Small_Red",
                 None, None, None)

Gren_Dino_Island64 = Room("Gren Dino Island 64", "SOOO you close to finishing your rage inducing trip"
                       "but you still have another one after this sooo, well never mind that but now you "
                       "are up against Marthplayed by Mew2King so don't let him grab you from across the stage",
                       "Marth played by Mew2king", None, None, "Dream_Land64", None)

Jungle_Japes = Room("Jungle Japs", "So they're finally here, performing for you If you know the words"
                    "you can join in to, Put you hand together, if you want to clap as we take you "
                    "through this monkey rap DK DONKEY KONG. Well you may have guessed it already that"
                    "your up against Donkey Kong king of the jungle so get ready to fight", "Donkey Kong",
                    None, None, "Kongo_Jungle", None)

Small_Red = Room("Small Red", "Small Red is a car not a map I don't know how you ended up on this car"
                 "but I am pretty sure the driver is kinda mad and he is well then there is Captain Falcon"
                 "Good luck because this man is really buff and has a very strong Knee so watch out for that",
                 "Captain Falcon", None, None, "Five_Sides", None)

Dream_Land64 = Room("Dream Land 64", "Well you got 2 rooms left if you have all the keys that is anyway"
                    "the last 2 are both bosses but this one is like a semi-boss so good luck cause "
                    "now you are up against Fox played by Armada", "Fox Played By Armada", None, "Final_Hallway",
                    "Key_Room", None)

Kongo_Jungle = Room("Kongo Jungle", "You mange to beat up DK but no Diddy Kong is mad at you so fight em cause"
                    "that is the only way to resolve anything in this world so get ready to fight ", "Diddy Kong",
                    None, "Good_Bay", None, None)

Five_Sides = Room("Five Sides", "Now you have fallen off of the super fast car that you were fighting on and"
                  "You have ended up in the big city but that doesn't mean you are free to do what ever you want"
                  "you still have a lot of people to fight just like now and your fighting Bowser who was here for"
                  "a brake but is fighting you now", "Bowser", None, None, "Onett", None)

Good_Bay = Room("")


current_node = journey_hallway
directions = ["north", "south", "east", "west"]
short_directions = ["n", "s", "e", "w"]

while True:
    print(current_node[''])  # Change
    print(current_node['**********'])  # Change
    command = input('>_'.lower())
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Look for which command we typed in
        pos = short_directions.index(command)
        command = directions[pos]
        # change command to be the long form
    if command in directions:
        try:
            print("hey")    # Change this
        except KeyError:
            print("You can not go back now keep fighting")
    if command == 'JV3':
        print("git gud")
    if command == 'Knock Knock':
        print("Knock-knock - it's Knuckles - the bloat thrower ")
        print("Independent flower ")
        print("Magical Emerald holder ")
        print("Give you the coldest shoulder ")
        print("My spike goes through boulders ")
        print("That's why I stay a loner ")
        print("I was born by myself ")
        print("I don't need a posse - I get it on by myself ")
        print("Adversaries get shelft")
    else:
        print('Command Not Recognized')

