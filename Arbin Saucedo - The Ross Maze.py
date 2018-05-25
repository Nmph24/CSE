class Item(object):
    def __init__(self, name):
        self.name = name

    def pick_up(self):
        print("You have picked up %s" % self.name)


class Statue(Item):
    def __init__(self, name, desc):
        super(Statue, self).__init__(name)
        self.desc = desc


class PaintBrushStatue(Statue):
    def __init__(self):
        super(PaintBrushStatue, self).__init__("Pain Brush Statue", "This statue shows that you just started playing "
                                               "this and mean that you are about to begin a probably easy maze but "
                                               "we will see so good luck")


class BobRossStatue(Statue):
    def __init__(self):
        super(BobRossStatue, self).__init__("Bob Ross Statue", "A Bob Ross Statue look nice and"
                                            " it is detailed greatly and it means you beat the game nice one"
                                            "I hope you read the paintings descriptions of you grabbed them if not "
                                            "that's fine but thanks for hanging out and beating the game now type "
                                            "quit to end the game Bye")


class Paintings(Item):
    def __init__(self, name, desc):
        super(Paintings, self).__init__(name)
        self.desc = desc


class WildernessDay(Paintings):
    def __init__(self):
        super(WildernessDay, self).__init__("Wilderness Day", "Wilderness Day was a painting and the " 
                                            "last one Bob Ross painted and it shows a forest with a sun "
                                            "down as it time and a path way made of rocks")


class InTheMidstOfWinter(Paintings):
    def __init__(self):
        super(InTheMidstOfWinter, self).__init__("In The Midst Of Winter", "In The Midst of Winter really "
                                                 "speaks for it self in it nice winter forest and it"
                                                 "small cabin and the trees around it that are dead."
                                                 "The winter is harsh but nice")


class LakeAtTheRidge(Paintings):
    def __init__(self):
        super(LakeAtTheRidge, self).__init__("Late At The Ridge", "This painting has a view of snowy mountains "
                                             " in the distant and a shining lake with a cloudy blue sky and green"
                                             "trees and grasses")


class BalmyBeach(Paintings):
    def __init__(self):
        super(BalmyBeach, self).__init__("Balmy Beach", "You can see an ocean with a sun down and a nice pink sky"
                                         "there are also some small waves crashing by and some palm trees")
        

class EvergreenValley(Paintings):
    def __init__(self):
        super(EvergreenValley, self).__init__("Evergreen Valley", "A nice snowy mountain in the distant and tall "
                                              "green trees with a small trail amd a pink blue sky in this painting")
    
    
class TrailsEnd(Paintings):
    def __init__(self):
        super(TrailsEnd, self).__init__("Trail's End", "This painting is showing a tree with no leaves in front "
                                        "but behind it there is a trail and a lot of orange autumn trees")
        
        
class BridgeToAutumn(Paintings):
    def __init__(self):
        super(BridgeToAutumn, self).__init__("Bridge To Autumn", "In This one there is a small wooden shelter "
                                             "with a lake behind it and the autumn trees on the other side of the "
                                             "lake and a small rock trail leading to the shelter")
       
        
class ViewFromClearCreek(Paintings):
    def __init__(self):
        super(ViewFromClearCreek, self).__init__("View From Clear Creek", "A site of a creek, a small river, tall"
                                                 "green grass and tall trees with mountains and hills in the distance"
                                                 "what a nice painting of this creek")
    
    
class CabinInTheHollow(Paintings):
    def __init__(self):
        super(CabinInTheHollow, self).__init__("Cabin In The Hollow", "A snowy forest with trees with pink leaves, "
                                               "a frozen lake, some fences and a cabin with snow on top this "
                                               "this painting really shows how it gets during winter in snowy areas")
    
    
class TranquilityCove(Paintings):
    def __init__(self):
        super(TranquilityCove, self).__init__("Tranquility Cove", "A painting with a river and some trees in the "
                                              "beginning of autumn with orange grenns grass and tress with the same "
                                              "color")


class WindingStream(Paintings):
    def __init__(self):
        super(WindingStream, self).__init__("Winding Stream", "This painting shows a trail, some tall trees next to "
                                            "it and mountains in the distant background with a blue sky")


class ReflectionsOfCalm(Paintings):
    def __init__(self):
        super(ReflectionsOfCalm, self).__init__("Reflections Of Calm", "This painting speaks for itself with the nice"
                                                "reflecting lake and the mountains in the back with trees and rocks "
                                                "surrounding the lake and a blue sky to top it all off")


class BlueRidgeFalls(Paintings):
    def __init__(self):
        super(BlueRidgeFalls, self).__init__("Blue Ridge Falls", "A nice waterfall that is being split by a rock "
                                             "surrounded but tall green trees and under it is the river current it"
                                             "is making what a nice painting")


class EveningsGlow(Paintings):
    def __init__(self):
        super(EveningsGlow, self).__init__("Evening's Glow", "Another Painting that can speak for itself. This one"
                                           "has a shining sun in the distant with a few mountains and its barely "
                                           "becoming day. It has a trail leading to a small cabin with trees behind"
                                           " it and a river as well next to it")


class SeasideHarmony(Paintings):
    def __init__(self):
        super(SeasideHarmony, self).__init__("Seaside Harmony", "A painting with the ocean and a cloudy pink sky with"
                                             "waves crashing against some rocks on the shore")


class AWalkInTheWoods(Paintings):
    def __init__(self):
        super(AWalkInTheWoods, self).__init__("A Walk In The Woods", "The first every painting Bob Ross made and "
                                              "it is pretty just like the rest. This painting has a small water "
                                              "lake with a trail leading towards it and autumn trees surrounding "
                                              "the trail and the small body of water with an yellow sky")

    
class You(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def note(self):
        print("%s " % self.name)


your_name = input("What is your name? ")
print("Nice to meet you %s" % your_name)

your_desc = input("Tell me a little something about yourself")

You = You("Desc Of You: %s is your name" % your_name, "and you are %s" % your_desc)

print(You.name, You. desc)


class Room(object):
    def __init__(self, name, description, s, n, e, w, items):
        self.name = name
        self.desc = description
        self.north = n
        self.south = s
        self.east = e
        self.west = w
        self.items = items

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


wilderness_day = WildernessDay()
bob_ross_statue = BobRossStatue()
in_the_midst_of_winter = InTheMidstOfWinter()
lake_at_the_ridge = LakeAtTheRidge()
balmy_beach = BalmyBeach()
evergreen_valley = EvergreenValley()
trails_end = TrailsEnd()
bridge_to_autumn = BridgeToAutumn()
view_from_clear_creek = ViewFromClearCreek()
cabin_in_the_hollow = CabinInTheHollow()
tranquility_cove = TranquilityCove()
winding_stream = WindingStream()
reflections_of_calm = ReflectionsOfCalm()
blue_ridge_falls = BlueRidgeFalls()
evenings_glow = EveningsGlow()
seaside_harmony = SeasideHarmony()
a_walk_in_the_woods = AWalkInTheWoods()
paint_brush_statue = PaintBrushStatue()

painters_beginning = Room("Painters Beginning", "Well this is gonna ba a great ride with a few items "
                          "not much there only really is paintings you can collect and they have some "
                          "reason to be there but you have to play to find out and this is a maze so "
                          "it might take some time so good luck with the maze also there is a random door?"
                          "walk through it if you want to but also some tips type 'look' to see all your "
                          "routes you can take anyway good luck", "Wilderness", None, None, None,
                          paint_brush_statue)

Wilderness = Room("Wilderness", "You walked through the door and the sun is just going down and there is "
                  "is a forest around you and a painting and another two doors you can grab the "
                  "painting if you want to up to you just type pick up then the name of the "
                  "item you want to pick up ", "Winter", "painters_beginning", "Lake", None,
                  wilderness_day)

Winter = Room("Winter", "The door must have sent you to a very snowy place but hey there is a cabin go inside..."
              "Well now you at least have shelter and there is a painting and if you want you can grab it also "
              "there is a door inside the cabin you want to go in?", None, 'Wilderness', "Beach", None,
              in_the_midst_of_winter)

Lake = Room("Lake", "It appears to be a lake and some mountains in the distant there is also another door and "
            "painting so might as well go to the door or if you want you can pick up that painting", "Beach", None,
            None, "Wilderness", lake_at_the_ridge)

Beach = Room("Beach", "You at the beach and it looks nice this place also has a sun about to sleep you can tell "
             "by the pink sky and there are two doors and another painting you can always pick it up if you want to"
             "that is", "Valley", "Lake", None, "Winter", balmy_beach)

Valley = Room("Valley", "You are on a trail after you got out the door and you can see the big snowy mountains"
              "and a lot of tall trees but it is a little cold. There is the painting and the doors again which"
              "you want ot go through and do you wan the painting?", "Autumn", "Beach", "Creek", "Trail",
              evergreen_valley)

Trail = Room("Trail", "Its an autumn forest with a lot of trees and another painting but no other doors here "
             "looks like your going ot hav to head back before you do, do you want the painting? Up to you.",
             None, None, 'Valley', None, trails_end)

Autumn = Room("Autumn",  "There is a small wooden shelter, a lake , and some trees but do you want to go in the "
              "small shelter?.... You walked in and there is a door and a painting do you want the painting and "
              "do you want ot head into the door?", None, "Valley", None, "Cabin", bridge_to_autumn)

Cabin = Room("Cabin", "Its freezing go into the cabin where its warm.... Your in and outside there are pink trees "
             "with snow on them and a frozen river there is also another painting in the room wanna grab it? No"
             "doors again well looks like you will have to head back again", None, None, "Autumn", None,
             cabin_in_the_hollow)

Creek = Room("Creek", "You are at a creek and it looks beautiful with trees on one side of a river and hill on the"
             " other there is also doors and a painting. who is leaving them behind? Anyway you wanna grab and go?",
             "Cove", "Stream", None, "Valley", view_from_clear_creek)

Cove = Room("Cove", "There is a river in front of you and some trees around but there are more in the distance."
            "There is the painting again, who would have guessed, anyway there is no doors again so we have to "
            "head back again but do you want to grab the painting before you go?", None, "Creek", None, None,
            tranquility_cove)

Stream = Room("Stream", "There is a trail in front of you and trees on the side of the trial there is also "
              "mountain in the distance and a blue sky not too cloudy either there is that painting again and "
              "some more doors so you wanna take the painting?", "Creek", "Reflection", "Seaside", None, winding_stream)

Reflection = Room("Reflection", "A big lake this time around and a closer mountain but still pretty far there are"
                  "also more trees and the painting also the door. So wanna grab the painting?", "Stream", None,
                  "Falls", None, reflections_of_calm)

Falls = Room("Falls", "Beautiful... a falls and a powerful stream and tons of trees and rocks following the stream"
             "there's the painting as usual but no door so we have to head back and if you want grab the painting to",
             None, None, None, "Reflection", blue_ridge_falls)

Seaside = Room("Seaside", "A beach and it looks pretty with the pink sky above and the clouds not to mention the "
               "crashing waves hitting the rocks. Oh the painting and door well if you want grab the painting if "
               "not don't up to you", "Evenings", None, None, "Stream", seaside_harmony)

Evenings = Room("Evenings", "A beautiful sun about to rise a nice stream some trees and a cabin... you walked in to"
                "he cabin and as expected the door and the painting so you want to or not up to you", "Walk", "Seaside",
                None, None, evenings_glow)

Walk = Room("Walk", "Well there is a trail and a small body of water in front of you and a nice autumn forest with a "
            "yellow sky and tons of trees and one last door and painting well take it or not i don't mind", "Art",
            "Evenings", None, None, a_walk_in_the_woods)

Art = Room("Art", "You made it to the end of the maze to a museum full of art and all kinds of it. It looks great"
           "well congrats on beating the maze and thanks for playing the game hope to see you soon and on more thing"
           "there is a statue grab it and read its description", None, "Walk", None, None, bob_ross_statue)

current_node = painters_beginning
directions = ["north", "south", "east", "west"]
short_directions = ["n", "s", "e", "w"]

bag_of_paintings = []

while True:
    print("Name: %s" % current_node.name)
    print("Desc: %s " % current_node.desc)
    if current_node.items is not None:
        print("Item: %s " % current_node.items.name)
    command = input('>_'.lower())
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You can not go that way")
    elif 'pick up' in command:
        item_req = input("What item? ")
        if item_req.lower() == current_node.items.name.lower():
            bag_of_paintings.append(current_node.items)
            print("Taken.")
        else:
            print("Item not Picked Up")
    elif "look at" in command:
        for Item in bag_of_paintings:
            if Item.name in command:
                print(Item.name)
                print(Item.desc)
    elif command == 'inventory':
        for Item in bag_of_paintings:
            print(Item.name)
    if command == 'Inventory':
        print(bag_of_paintings)
    if command == 'Bob':
        print("very art")
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
    if command == "Kappa":
      print("░░░░░░░░░")
      print("░░░░▄▀▀▀▀▀█▀▄▄▄▄░░░░")
      print("░░▄▀▒▓▒▓▓▒▓▒▒▓▒▓▀▄░░")
      print("▄▀▒▒▓▒▓▒▒▓▒▓▒▓▓▒▒▓█░")
      print("█▓▒▓▒▓▒▓▓▓░░░░░░▓▓█░")
      print("█▓▓▓▓▓▒▓▒░░░░░░░░▓█░")
      print("▓▓▓▓▓▒░░░░░░░░░░░░█░")
      print("▓▓▓▓░░░░▄▄▄▄░░░▄█▄▀░")
      print("░▀▄▓░░▒▀▓▓▒▒░░█▓▒▒░░")
      print("▀▄░░░░░░░░░░░░▀▄▒▒█░")
      print("░▀░▀░░░░░▒▒▀▄▄▒▀▒▒█░")
      print("░░▀░░░░░░▒▄▄▒▄▄▄▒▒█░")
      print("░░░▀▄▄▒▒░░░░▀▀▒▒▄▀░░")
      print("░░░░░▀█▄▒▒░░░░▒▄▀░░░")
      print("░░░░░░░░▀▀█▄▄▄▄▀")
    if command == "look":
        print("East: %s " % current_node.east)
        print("North: %s " % current_node.north)
        print("South: %s " % current_node.south)
        print("West: %s " % current_node.west)
