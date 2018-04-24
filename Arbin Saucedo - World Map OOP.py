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


journey_hallway = Room("Journey Hall", "You have arrived at a hallway that will lead you into "
                       "many battles in this world and you need show your the best fighter out there",
                       None, 'Temple', None, 'TangerineCastle', None)

Temple = Room("Temple", "This Temple is where your first fight begins"
              "with Princess Zelda good luck with the fight and the others that come with many more"
              "fighters you will face", "Zelda", "ColdPlace", None, "Fountain_Of_Sleep",
              None)

TangerineCastle = Room("Tangerine Castle", "The Castle of the Olive Kingdom and your first fight "
                       "with Princess Tangerine", "Princess Peach", "Fountain_Of_Sleep", None,
                       "Olive_Kingdom", None)

FountainOfSleep = Room("FountainOfSleep", "Now you are extra sleepy but you can fight still "
                       "so be happy for that but you now you up against "
                       "a harder characters because you have chosen the short "
                       "but harder path to the end so you are up against "
                       "Jigglypuff", "Jigglypuff played by HBox", None, None,
                       "BlueBlues", None)

OliveKingdom = Room("Olive Kingdom", "This is the Olive Kingdom the home of Mario,"
                    "Dr.Mario, and Luigi and here you will be Fighting Mario so START"
                    , "Mario", None, None, "OliveKingdom2", None)

ColdPlace = Room("Cold Place", "The Coldest place out of this whole world"
                 "which is also mount everest and here you "
                 "are fighting 2 people that are one fighther"
                 "Ice Climbers", "Ice Climbers", "LoudCity", None, None, None)

BlueBlues = Room("Blue Blues", "Now it gets harder from here in blue blues so now "
                 "your up against Sheik played by Plup ,so good luck cause its a top tier",
                 "Shiek", None, None, "GrenDinoIsland64",None)

OliveKingdom2 = Room("Olive Kingdom 2", "This is the other side of the Olive Kingdom where you "
                     "are slowly entering the jungle to fight someone else "
                     "but for now you up against Luigi", "Luigi", None, None, "Jungle_Japes", None)

LoudCity = Room("Loud City", "Well your in the city know and well this place looks like it has more of "
                "an advance in car technology and there is still fighters here so don't"
                "let the cars distract you anyways now your up against Pichu a small mice but "
                "don't let that fool you he still packs a good punch", "Pichu", "Small_Red",
                None, None, None)

GrenDinoIsland64 = Room("Gren Dino Island 64", "SOOO you close to finishing your rage inducing trip"
                        "but you still have another one after this sooo, well never mind that but now you "
                        "are up against Marth so don't let him grab you from across the stage",
                        "Marth", None, None, "Dream_Land64", None)

JungleJapes = Room("Jungle Japs", "So they're finally here, performing for you If you know the words"
                   "you can join in to, Put you hand together, if you want to clap as we take you "
                   "through this monkey rap DK DONKEY KONG. Well you may have guessed it already that"
                   "your up against Donkey Kong king of the jungle so get ready to fight",
                   "Donkey Kong", None, None, "Kongo_Jungle", None)


Small_Red = Room("Small Red", "Small Red is a car not a map I don't know how you ended up on this car"
                 "but I am pretty sure the driver is kinda mad and he is well then there is Captain Falcon"
                 "Good luck because this man is really buff and has a very strong Knee so watch out for that",
                 "Captain Falcon", None, None, "Five_Sides", None)

Dream_Land64 = Room("Dream Land 64", "Well you got 2 rooms left if you have all the keys that is anyway"
                    "the last 2 are both bosses but this one is like a semi-boss so good luck cause "
                    "now you are up against Fox", "Fox", None,
                    "Final_Hallway", "Key_Room", None)

Kongo_Jungle = Room("Kongo Jungle", "You mange to beat up DK but no Diddy Kong is mad at you so fight em cause"
                    "that is the only way to resolve anything in this world so get ready to fight ",
                    "Diddy Kong", None, "Good_Bay", None, None)

Five_Sides = Room("Five Sides", "Now you have fallen off of the super fast car that you were fighting on and"
                  "You have ended up in the big city but that doesn't mean you are free to do what ever you want"
                  "you still have a lot of people to fight just like now and your fighting Bowser who was here for"
                  "a brake but is fighting you now", "Bowser", None, None, "Onett", None)

Good_Bay = Room("Good Bay", "Well you made it out of the jungle but now your in a nice bay area"
                "very pretty place but that does not mean you journey is over you still have "
                "a long way to go but now you are fighting Link", "Link", "Pokefloats", None,
                None, None)

Onett = Room("Onett", "You left the big city after your fight with Bowser and now your in a small "
             "town and your at its medicine shop called Onett but your still not done fighting"
             "you are fighting Ness in his home town and he is not or normal kid watch out", "Ness",
             None, None, "Corneria", None)

Pokefloats = Room("Pokefloats", "You manage to beat Link but you somehow get to a float show with many "
                  "floats from pokemon and you happen to land on one of them and they start to inflate them"
                  "so now your in the air but there is still a challenger and his name is Pikachu", "Pikachu",
                  "Pokestadium", None, None, None)

Corneria = Room("Cornria", "Away from the small city you get on a ship to get away but there is someone "
                "else in the ship he shoots at you and you jump on top of the ship and there is the "
                "captain of the ship Falco the blue bird of the glaxies and he is your next opponent",
                "Falco", None, None, "Venom", None)

Pokestadium = Room("Pokestadium", "You made it off the floats and won against Pikachu but you now your at "
                   "a stadium for pokemon fights and you feel a weird pressure coming from the shadows "
                   "then a ball of dark energy launches at you but you dodge it and now your next fight"
                   "begins against Mewtwo careful not to look him in the eyes up close he has a special "
                   "that confuses you to get comboed so take care ", "Mewtwo", None, None, None,
                   "Rainbowcruise")

Venom = Room("Venom", "That should have been the only person there but there was someone else on the ship"
             "Young Link jumps out on top of the ship with you. He was trying to catch a ride like you to go"
             "go back home with it but he is the last one on here and he crashed the engine so your going to"
             "falling down soon so good luck", "Young Link", None, None, None, "Brinstar")

Rainbowcruise = Room("Rainbowcruise", "Now you got out the stadium and won and you see a cruise ship in the "
                     "distant so you board it but there is no breaks in this game so get ready cause your next "
                     "is on this ship and his name is Yoshi and he is a small green dinosaur but he does "
                     "really look the part but watch out for his tongue", "Yoshi", None, None, "Flatzone", None)

Brinstar = Room("Brinstar", "The ship crashed onto a mountain side and now it is a weird valcano like area "
                "but its green acid instead of lava and your not safe either there is still fighting even in"
                "place and its Samus a bounty hunter of space and she is here to get you so take care and watch "
                "cause she knows her stuff", "Samus", None, None, "BrinstarDepths", None)

Flatzone = Room("Flatzone", "You somehow made it into a video game inside of a video game and your in a 2d "
                "area against Mr. Game And Watch who is the owner of the place and he wants you out so you gotta "
                "go against him now and tip watch out for his judgement hammer it deals crazy damage", "MrGameAndWatch"
                , "KongoJungle64", None, None, None)

Brinstardepths = Room("Brinstardepths", "You survived against a bounty hunter thats good but you fell far down and "
                      "somehow survived oh well its a game anything can happen anyway your not done fighting there "
                      "is someone with you and yes there is and he is Ganondorf the dark warlock also this place"
                      "is ready to explode like a volcano", "Ganondorf", None, "GrenDinoIsland", None, None)


KongoJungle64 = Room("KongoJungle64", "Game and watch let you go after you beat him and showed you the way out"
                     "or did he. You end up in a familar jungle but you are fighting kirby instead of DK or "
                     "Diddy Kong but anyway don't let Kirby hit you with his flaming hammer or it will hurt"
                     ". Just saying your close to the end", "Kirby", None, "Keyroom", None, "TheEndHall")

GrenDinoIsland = Room("GrenDinoIsland", "Your on a island looks like heaven or something but its peaceful "
                      "maybe you died to the explosion after beating Ganondorf but there is someone with a sword"
                      "and his name is Roy and he is a skilled swords man also he has magic powers that can bind "
                      "with his sword so careful for that anyway your close to finishing this game", "Roy",
                      "Keyroom", None, None, "TheEndHall")

Keyroom = Room("Keyroom", "Your in a hallway leading you to 3 different rooms choose the one you haven't been to"
               "yet", None, None, "DreamLand64", "KongoJungle64", "GrenDinoIsland")

TheEndHall = Room("TheEndHall", "This is the end hall that will lead you to the last 2 battles with actual bosses"
                  "and it won't be easy good luck", None, None, None, "Battlefield", None)

Battlefield = Room("Battlefield", "This is Crazy hand, he is just a hand with white glove but he is crazy and an "
                   "odd one with many attacks and more health also he is really fast so you better come up with "
                   "a way to beat him", "CrazyHand", None, None, "FinalDestination", None)

FinalDestination = Room("FinalDestination", "You beat Crazy Hand props to you but there is one more hand "
                        "the one who started this all Master Hand. He is the final boss to this world and the "
                        "only way to beat the game is to beat him but he is careful with what he does and has "
                        "a lot of health so good luck", "MasterHand", None, None, "Victory", None)

Victory = Room("Victory", "You did it you won the game I hope this was a good game and not bad anyway thanks"
               "for playing bye", None, None, None, None, None)

current_node = journey_hallway
directions = ["north", "south", "east", "west"]
short_directions = ["n", "s", "e", "w"]

while True:
    print(current_node.desc)
    print(current_node.name)  # Change
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
            current_node.move(command)
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
    if command == "look":
        print(current_node.fighters)
        print(current_node.east)
        print(current_node.north)
        print(current_node.south)
        print(current_node.west)

